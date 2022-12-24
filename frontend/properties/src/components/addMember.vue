<template>
    <div class="text-center">
        <v-dialog
          :value="activate"
          width="700"
          height="600"
        >
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
                            v-model="property_name"
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
              <v-btn
                
                color="red"
                text
                @click="$emit('closedDialog')"
              >
                Cancel
              </v-btn>
              <v-btn
                :loading="loading"
                color="indigo white--text"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </template>
    
<script>
export default {
    name: 'addMember',
    props: {
        activate: Boolean
    },
    data: () => ({
        /* --- DYNAMIC DATA --- */
        property_name: null,
        selectedRooms: [],

        /* --- STATIC DATA --- */

        /* --- LOADING STATUS --- */
        loading: false,
    }),
    methods : {

    }
}
</script>