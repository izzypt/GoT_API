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
				<v-icon  class="mr-3" filled rounded color="white">mdi-delete</v-icon> Delete House
			</v-card-title>
			<!-- CONTENT -->
			<v-card-text class="mt-2 pa-6">
				Please make sure you want to delete this house !
			</v-card-text>
			<v-divider></v-divider>
			<!-- ACTIONS -->
			<v-card-actions>
				<v-spacer class="my-2"></v-spacer>
				<v-btn
					text
					@click="$emit('closedDialog')"
				>
					Cancel
				</v-btn>
				<v-btn
					:loading="loading"
					color="red white--text"
					@click="deleteHouse"
				>
					Delete
				</v-btn>
			</v-card-actions>
			</v-card>
		</v-dialog>
	</div>
</template>

<script>
import gql from 'graphql-tag'

export default {
	name: 'DeleteDialog',
	props : ["activate", "deleteID"],
	data: () => ({
		loading: false,
		tempID: null,
	}),
   methods : {
		deleteHouse() {
			console.log(this.deleteID)
			console.log(typeof this.deleteID)
			this.loading = true
			this.$apollo.mutate({
				mutation: gql`
       				mutation deleteHouse($id: Int!) {
          				deleteHouse(id: $id) {
            				house{
              					id
              					name
            				}
          				}
        			}`,
					variables: {
						id: parseInt(this.deleteID),
					},                
				})
			.then(data => {
				console.log(data)
				this.loading = false;
				this.$emit('deletedHouse')
				this.$emit('closedDialog')
			})
		}
    }
}
</script>