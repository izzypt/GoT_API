<template>
  <div class="text-center">
    <v-dialog :value="activate" width="700" height="600">
      <!-- TITLE -->
      <v-card>
        <v-card-title class="indigo white--text text-h5">
          <v-icon filled rounded color="white">mdi-plus</v-icon> Add member
        </v-card-title>
        <!-- CONTENT -->
        <v-card-text class="mt-2 pa-6">
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="member_name"
                label="Name"
                outlined
                filled
                prepend-icon="mdi-account"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <!-- ACTIONS -->
        <v-card-actions>
          <v-spacer class="my-2"></v-spacer>
          <v-btn color="red" text @click="$emit('closedDialog')">
            Cancel
          </v-btn>
          <v-btn
            :loading="loading"
            color="indigo white--text"
            @click="addMember"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import gql from "graphql-tag"
export default {
  name: "addMember",
  props: ["activate", "selectedID"],
  data: () => ({
    /* --- DYNAMIC DATA --- */
    member_name: null,
    selectedRooms: [],

    /* --- STATIC DATA --- */

    /* --- LOADING STATUS --- */
    loading: false,
  }),
  methods: {
	addMember(){
		console.log(this.member_name, this.selectedID)
		this.$apollo.mutate({
			mutation: gql`
			mutation($houseId: Int!, $name: String!){
				createMember(houseId: $houseId, name:$name){
					member{
						id,
						name
					}
				}
			}`,
			variables : {
				houseId: parseInt(this.selectedID),
				name: this.member_name
			}
		})
		.then(data => {
			console.log(data)
			this.$emit('closedDialog')
			this.$emit('AddedMember')
		})
	}
  },
};
</script>
