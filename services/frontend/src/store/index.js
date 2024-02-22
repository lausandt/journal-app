import { createStore } from "vuex";

import entries from './modules/entries';
import users from './modules/users';

export default createStore({
  modules: {
    entries,
    users,
  }
});