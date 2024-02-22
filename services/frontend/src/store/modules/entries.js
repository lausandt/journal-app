import axios from 'axios';

const state = {
  entries: null,
  entry: null
};

const getters = {
  stateEntries: state => state.entries,
  stateEntry: state => state.entry,
};

const actions = {
  async createEntry({dispatch}, form) {
    // let date = new Date(form.created_at)
    // form.created_at = date.toISOString()
    await axios.post('entries/create entry', form);
    await dispatch('getMyEntries');
  },
  async getMyEntries({commit}) {
    let {data} = await axios.get('entries/my entries');
    commit('setEntries', data);
  },
  async viewEntry({commit}, id) {
    let {data} = await axios.get(`entries/view entry/${id}`);
    commit('setEntry', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateEntry({}, entry) {
    await axios.patch(`entries/update entry/${entry.id}`, entry.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteEntry({}, id) {
    await axios.delete(`entries/delete entry/${id}`);
  }
};

const mutations = {
  setEntries(state, entries){
    state.entries = entries;
  },
  setNote(state, entry){
    state.entry = entry;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};