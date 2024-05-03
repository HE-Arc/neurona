import {ref} from "vue";

class MessageManager {
  constructor() {
    if (MessageManager.instance) {
      return MessageManager.instance;
    }
    MessageManager.instance = this;
    this.messages = ref([]);
    this.snack = ref({});
  }

  static getInstance() {
    if (!MessageManager.instance) {
      MessageManager.instance = new MessageManager();
    }
    return MessageManager.instance;
  }

  add(severity, message, timeout = 5000) {
    if(message === undefined) {
      message = "An unknown error occurred";
    }
    this.messages.value = [{
      type: severity,
      message: [message]
    }];
    setTimeout(() => {
      this.messages.value = [];
    }, timeout);
  }

  snackbar(message, timeout = 2000){
    this.snack.value = {
      message: message,
      timeout: timeout
    }
  }

  clearSnackbar(){
    this.snack.value = {};
  }

  get() {
    return this.messages;
  }

  getSnackbar(){
    return this.snack;
  }
}

export default MessageManager;
