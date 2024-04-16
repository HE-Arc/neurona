import axios from "axios";
import routes from "@/api/routes";

async function fetchRegisterOptions(username, name) {
  return axios.post(routes.authentication.register_options, {
    "username": username,
    "display_name": name,
  });
}

async function fetchLoginOptions(username) {
  return axios.post(routes.authentication.login_options, {
    "username": username,
  });
}

function strToBuf(str) {
  str = str.replace(/-/g, '+').replace(/_/g, '/');
  return Uint8Array.from(
    atob(str), c => c.charCodeAt(0))
}

function BufToBase64url(buf) {
  let str = '';
  let bytes = new Uint8Array(buf);
  for (let i = 0; i < bytes.byteLength; i++) {
    str += String.fromCharCode(bytes[i]);
  }
  let base64 = btoa(str);
  return base64
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

async function getRegisterCredentialOptions(username, name) {
  const options_str = await fetchRegisterOptions(username, name);
  const options = JSON.parse(options_str.data.options);
  const challenge_id = options_str.data.id;

  options.challenge = strToBuf(options.challenge);
  options.user.id = strToBuf(options.user.id);

  return {
    options: options,
    challenge_id: challenge_id,
  }
}

async function getLoginCredentialOptions(username_or_email) {
  const options_str = await fetchLoginOptions(username_or_email);
  const options = JSON.parse(options_str.data.options);
  const challenge_id = options_str.data.id;

  options.challenge = strToBuf(options.challenge);

  return {
    options: options,
    challenge_id: challenge_id,
  }
}

async function createPublicKeyCredential(username, name) {
  const credentialOptions = await getRegisterCredentialOptions(username, name);
  const credentials_ = await navigator.credentials.create({publicKey: credentialOptions.options});

  const credentials = {
    id: credentials_.id,
    rawId: credentials_.id,
    response: {
      attestationObject: BufToBase64url(credentials_.response.attestationObject),
      clientDataJSON: BufToBase64url(credentials_.response.clientDataJSON),
    },
    type: credentials_.type,
  }

  const challenge_id = credentialOptions.challenge_id;

  return {
    credentials: credentials,
    challenge_id: challenge_id,
  }
}

async function getPublicKeyCredential(username_or_email) {
  const credentialOptions = await getLoginCredentialOptions(username_or_email);
  const credentials_ = await navigator.credentials.get({publicKey: credentialOptions.options});

  const credentials = {
    id: credentials_.id,
    rawId: credentials_.id,
    response: {
      authenticatorData: BufToBase64url(credentials_.response.authenticatorData),
      clientDataJSON: BufToBase64url(credentials_.response.clientDataJSON),
      signature: BufToBase64url(credentials_.response.signature),
      userHandle: BufToBase64url(credentials_.response.userHandle),
    },
    type: credentials_.type,
  }

  return {
    credentials: credentials,
    challenge_id: credentialOptions.challenge_id,
  }
}

async function requestLogin(username, credentials, challenge_id) {
  const data = {
    credentials: credentials,
    data: {
      challenge_id: challenge_id,
      username: username,
    }
  }

  return await axios.post(routes.authentication.login, data);
}

async function requestRegister(username, name, credentials, challenge_id) {
  const data = {
    credentials: credentials,
    data: {
      username: username,
      display_name: name,
      challenge_id: challenge_id
    }
  }

  return await axios.post(routes.authentication.register, data);
}

async function login(username) {
  const credentials = await getPublicKeyCredential(username);
  return await requestLogin(username, credentials.credentials, credentials.challenge_id);
}

async function register(username, name){
  const credentials = await createPublicKeyCredential(username, name);
  return await requestRegister(username, name, credentials.credentials, credentials.challenge_id);
}


export {register, login};
