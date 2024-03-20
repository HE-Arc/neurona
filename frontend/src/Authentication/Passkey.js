import axios from "axios";
import routes from "@/api/routes";

async function fetchRegisterOptions(username, email) {
  console.log("route", routes.authentication.register_options);
  return axios.post(routes.authentication.register_options, {
    "username": username,
    "email": email,
  });
}

async function fetchLoginOptions(username_or_email) {
  return axios.post(routes.authentication.login_options, {
    "username_or_email": username_or_email,
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

async function getRegisterCredentialOptions(username, email) {
  const options_str = await fetchRegisterOptions(username, email);
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

async function createPublicKeyCredential(username, email) {
  const credentialOptions = await getRegisterCredentialOptions(username, email);
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

async function requestLogin(username_or_email, credentials, challenge_id) {
  const data = {
    credentials: credentials,
    data: {
      challenge_id: challenge_id,
      username_or_email: username_or_email,
    }
  }

  return await axios.post(routes.authentication.login, data);
}

async function requestRegister(username, email, credentials, challenge_id) {
  const data = {
    credentials: credentials,
    data: {
      username: username,
      email: email,
      challenge_id: challenge_id
    }
  }

  await axios.post(routes.authentication.register, data);
}

async function login(username_or_email) {
  const credentials = await getPublicKeyCredential(username_or_email);
  const response = await requestLogin(username_or_email, credentials.credentials, credentials.challenge_id);
  return response;
}

async function register(username, email){
  const credentials = await createPublicKeyCredential(username, email);
  await requestRegister(username, email, credentials.credentials, credentials.challenge_id);
}


export {register, login};
