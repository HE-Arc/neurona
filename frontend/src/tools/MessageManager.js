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
    console.log("adding message", severity, message);
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
