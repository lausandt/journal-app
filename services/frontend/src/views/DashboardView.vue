<template>
    <div>
      <section>
        <h1>Add new entry</h1>
        <hr/><br/>
  
        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="title" class="form-label">Title:</label>
            <input type="text" name="title" v-model="form.title" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="amount" class="form-label">Amount:</label>
            <input type="number" step="0.01" name="amount" v-model="form.amount" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="supplier" class="form-label">Supplier:</label>
            <input type="text" name="supplier" v-model="form.supplier" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="qualification" class="form-label">Choose a qualification for this entry:</label>
            <select name="qualification" v-model="form.qualification">
              <option value="Need">Need</option>
              <option value="Want">Want</option>
              <option value="Leisure">Leisure</option>
              <option value="Unexpected">Unexpected</option>
            </select>
          </div> 
          <div class="mb-3">
            <label for="note" class="form-label">Note:</label>
            <textarea
              name="note"
              v-model="form.note"
              class="form-control"
            ></textarea>
          </div>
          <!-- <div class="mb-3">
            <label for="created_at" class="form-label">Date:</label>
            <input type="date" name="created_at" v-model="form.date" class="form-control" />
          </div> -->
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </section>
  
      <br/><br/>
  
      <!-- <section>
        <h1>Entries</h1>
        <hr/><br/>
  
        <div v-if="entries.length">
          <div v-for="entry in entries" :key="entry.id" class="entries">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <ul>
                  <li><strong>Title:</strong> {{ entry.title }}</li>
                  <li><strong>Author:</strong> {{ entry.author.username }}</li>
                  <li><router-link :to="{name: 'Note', params:{id: entry.id}}">View</router-link></li>
                </ul>
              </div>
            </div>
            <br/>
          </div>
        </div>
  
        <div v-else>
          <p>Nothing to see. Check back later.</p>
        </div>
      </section> -->
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Dashboard',
    data() {
      return {
        form: {
          title: '',
          amount:0.00,
          supplier:'',
          qualification:'',
          note: '',
          created_at: '2024-02-22',
        },
      };
    },
    created: function() {
      return this.$store.dispatch('getMyEntries');
    },
    computed: {
      ...mapGetters({ entries: 'stateEntries'}),
    },
    methods: {
      ...mapActions(['createEntry']),
      async submit() {
        await this.createEntry(this.form);
      },
    },
  });
  </script>
  