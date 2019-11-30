<template>
    <div class="added-component">
        <h1>Your Names</h1>
        <div v-if="loggedInUser" class="added-container">
            <ul>
                <li v-for="name in nameList" :key='name.id'>{{name}}</li>
            </ul>
        </div>
        <div v-else> 
            <p>Please login to view your favorite names</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'addedNames',
    data() {
        return {
            loggedInUser: '',
            nameList: [],
        }
    },
    methods: {
        getSessionName() {
            axios.post('/users')
            .then((resp) => {
                this.loggedInUser = resp.data.userInSession
                this.getNames()
            })
        },
        getNames() {
            axios.post('/user-added-names', {
                name_owner: this.loggedInUser
            })
            .then((resp) => {
                this.nameList = resp.data.name_list
            })
        }
    },
    mounted() {
        this.getSessionName()
    }
}

</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
</style>