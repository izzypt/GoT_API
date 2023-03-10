<template>
  <v-card>
    <!-- TITLE -->
    <v-card-title class="indigo white--text text-h5">
      The Great Houses of the Seven Kingdoms
    </v-card-title>

    <v-row class="pa-4" justify="space-between">
      <!-- LEFT SIDE (LIST + ADD PROPERTY BUTTON) -->
      <v-col cols="5">
        <v-treeview
          :active.sync="active"
          :items="houses"
          :open.sync="open"
          activatable
          color="warning"
          open-on-click
          transition
        >
          <template v-slot:prepend="{ item }">
            <v-icon v-if="!item.children"> mdi-home </v-icon>
          </template>
        </v-treeview>
        <v-divider></v-divider>
        <!-- FILTER + ADD PROPERTY-->
        <v-row class="mt-5">
          <v-spacer></v-spacer>
          <v-col cols="3" class="d-flex justify-end">
            <v-btn
              small
              class="mt-6"
              color="indigo white--text"
              @click="openAddDialog"
              >Add House</v-btn
            >
          </v-col>
        </v-row>
      </v-col>

      <v-divider vertical></v-divider>
      <!-- RIGHT SIDE (PROPERTY DETAILS + DELETE) -->
      <v-col class="d-flex text-center">
        <v-scroll-y-transition mode="out-in">
          <!-- IF NO SELECTED PROPERTY -->
          <div
            v-if="!selected"
            class="text-h6 grey--text text--lighten-1 font-weight-light"
            style="align-self: center"
          >
            Select a House
          </div>
          <!-- IF SELECTED PROPERTY -->
          <v-card
            v-else
            :key="selected.id"
            class="pt-1 mx-auto"
            flat
            max-width="800"
          >
            <v-card-text width="600" name="house_image">
              <v-avatar v-if="selected?.banner" size="98">
                <v-img :src="`${selected?.banner}`" class="mb-6"></v-img>
              </v-avatar>
              <h3 class="text-h4 mb-2">
                {{ selected?.name }}
              </h3>

              <v-divider></v-divider>
              <v-row class="text-left">
                <v-col class="my-3">
                  <li v-for="(member, i) in selected?.membersSet" :key="i">
                    {{ member.name }}
                    <v-icon class="ml-2" small @click="memberEditDialog(member, false)">mdi-pencil</v-icon>
                  </li>
                </v-col>
              </v-row>
              <!-- EDIT DIALOG-->
              <v-dialog width="300" v-model="snackbar" elevation="2" :vertical="true">
                    <v-card>
                        <v-card-title class="indigo white--text text-h5">
                            <v-icon class="mr-2" color="white">mdi-pencil</v-icon>Edit Name
                        </v-card-title>
                        <v-card-text class="mt-2 pa-6">
                            <v-text-field v-model="selectedMember.name" label="Name" outlined></v-text-field>
                        </v-card-text>
                   

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="red"
                            text
                            @click="snackbar = false"
                      >
                        Cancel
                      </v-btn>
                      <v-btn
                      @click="memberEditDialog(false, true)"
                        color="indigo white--text"
                      >
                        Save
                      </v-btn>
                    </v-card-actions>
                </v-card>
                  </v-dialog>
              <v-row class="d-flex justify-center ma-2">
                <v-btn
                  x-small
                  class="my-2 mx-1"
                  color="indigo white--text"
                  @click="openAddMember = true"
                  >Add member</v-btn
                >
                <v-btn
                  x-small
                  class="my-2 mx-1 white--text"
                  color="red"
                  @click="openDeleteDialog = true"
                >
                  Delete
                </v-btn>
              </v-row>
            </v-card-text>
          </v-card>
        </v-scroll-y-transition>
      </v-col>
    </v-row>
    <!-- DIALOGS -->
    <AddHouseDialog
      :activate="openAddHouseDialog"
      v-on:closedDialog="openAddHouseDialog = !openAddHouseDialog"
      v-on:addedHouse="$apollo.queries.allHouses.refetch()"
    ></AddHouseDialog>

    <AddMember
      :activate="openAddMember"
      :selectedID="selected?.id"
      v-on:AddedMember="$apollo.queries.allHouses.refetch()"
      v-on:closedDialog="openAddMember = !openAddMember"
    ></AddMember>

    <DeleteDialogVue
      :activate="openDeleteDialog"
      :deleteID="selected?.id"
      v-on:closedDialog="openDeleteDialog = !openDeleteDialog"
      v-on:deletedHouse="$apollo.queries.allHouses.refetch()"
    >
    </DeleteDialogVue>
  </v-card>
</template>

<script>
import AddHouseDialog from "./addHouseDialog.vue";
import AddMember from "./addMember.vue";
import DeleteDialogVue from "./deleteDialog.vue";
import gql from "graphql-tag";

export default {
  name: "PropriedadesComponente",
  components: {
    AddHouseDialog,
    AddMember,
    DeleteDialogVue,
  },
  props: {
    msg: String,
  },
  apollo: {
    allHouses: gql`
      query {
        allHouses {
          id
          name
          banner
          membersSet {
            id
            name
          }
        }
      }
    `,
  },
  data: () => ({
    /* --- DATA CONTAINERS --- */
    active: [],
    open: [],
    allHouses: [],

    /* --- DYNAMIC DATA */
    selectedMember: {
        id : null,
        name : null,
    },

    /* --- DIALOG STATUS --- */
    openAddHouseDialog: false,
    openAddMember: false,
    openDeleteDialog: false,
    snackbar: false,
  }),

  computed: {
    houses() {
      return [
        {
          name: "Houses",
          children: this.allHouses,
        },
      ];
    },
    selected() {
      if (!this.active.length) return undefined;

      const id = this.active[0];

      return this.allHouses.find((house) => house.id === id);
    },
  },

  watch: {},
  methods: {
    pause(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    openAddDialog() {
      this.openAddHouseDialog = true;
    },
    memberEditDialog(member, edit){
        this.snackbar = true
        if (member)
            this.selectedMember = member
        console.log(this.selectedMember.id)
        console.log(this.selectedMember.name)
        if (edit)
        {
            this.$apollo.mutate({
                mutation : gql`
                    mutation($id: ID, $name: String){
                        updateMember(id: $id, name:$name){
                            member {
                                id
                                name
                            }
                        }
                    }`, 
                    variables : {
                        id : this.selectedMember.id,
                        name : this.selectedMember.name
                    }
                }).then(data => {
                    console.log(data);
                    this.snackbar = false;
                })
            }
    }
  },
};
</script>
