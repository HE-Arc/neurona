//TODO add env file for the host
const HOST = process.env.PASSKEY_HOST;

//TODO : get the challenge from the server
function randomStringFromServer() {
  const length = 32;
  let result = '';
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const charactersLength = characters.length;
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

function userIdFromEmail(email) {
  const id = Uint8Array.from(
    email, c => c.charCodeAt(0)
  );
  console.log("generated id", id);
  return id;
}

function getPublicKeyOptions(name, email) {
  return {
    challenge: Uint8Array.from(
      randomStringFromServer(), c => c.charCodeAt(0)),
    rp: {
      name: "NeuronaAuth",
      id: HOST
    },
    user: {
      id: userIdFromEmail(email),
      name: email,
      displayName: name,
    },
    pubKeyCredParams: [{alg: -7, type: "public-key"}],
    authenticatorSelection: {
      authenticatorAttachment: "cross-platform",
    },
    timeout: 60000,
    attestation: "direct"
  };
}

function getPublicKeyCredentialOptions(email) {
  return {
    challenge: Uint8Array.from(
      randomStringFromServer(), c => c.charCodeAt(0)),
    allowCredentials: [{
      id: userIdFromEmail(email),
      type: 'public-key',
      transports:
        [
          "usb",
          "nfc",
          "smart-card",
          "hybrid",
          "ble",
          "internal",
        ],
    }],
    timeout: 60000,
  }
}

function createPublicKeyCredential(name, email) {
  const publicKeyCredentialCreationOptions = getPublicKeyOptions(name, email);
  return navigator.credentials.create({publicKey: publicKeyCredentialCreationOptions});
}

function getCredentials(email) {
  const publicKeyCredentialOptions = getPublicKeyCredentialOptions(email);
  return navigator.credentials.get({publicKey: publicKeyCredentialOptions});
}

export {createPublicKeyCredential, getCredentials};
