import {ref} from "vue";

class MessageManager {
  constructor() {
    if (MessageManager.instance) {
      return MessageManager.instance;
    }
    MessageManager.instance = this;
    this.messages = ref([]);
  }

  static getInstance() {
    if (!MessageManager.instance) {
      MessageManager.instance = new MessageManager();
    }
    return MessageManager.instance;
  }

  add(severity, message) {
    if(message === undefined) {
      message = "An unknown error occurred";
    }
    this.messages.value.push({
      type: severity,
      message: [message]
    });
  }

  get() {
    return this.messages;
  }
}

export default MessageManager;
