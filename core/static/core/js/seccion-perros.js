new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        country_flag_url: "",
        images: [],
        breeds: [],
        selected_breed: {},
        current_image: {}
    },
    created() {
        this.getBreeds();
    },
    watch: {

        selected_breed: function () {
            console.log(this.selected_breed)

            

            this.country_flag_url = 'https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.2.1/flags/1x1/${country_code}.svg';
            this.getImages();
        }
    },
    methods: {

        async getBreeds() {
            try {
                axios.defaults.headers.common['x-api-key'] = "core" // Replace this with your API Key, as it's set to defaults it will be used from now onwards

                let response = await axios.get('https://api.thedogapi.com/v1/breeds/')
                this.breeds = response.data;
                console.log("-- (" + this.breeds.length + ") Breeds from TheDogAPI.com")

                // pick one to display initially
                this.selected_breed = this.breeds[10]
            } catch (err) {
                console.log(err)
            }
        },
        async getImages() {
            try {

                let query_params = {
                    breed_id: this.selected_breed.id
                }
                console.log (this.selected_breed.id);
                let response = await axios.get('https://api.thedogapi.com/v1/images/search', { params: query_params })

                this.pagination_count = response.headers['pagination-count'];
                this.images = response.data
                this.current_image = this.images[0]



                console.log("-- (" + this.images.length + ") Images from TheDogAPI.com")
                console.log(this.pagination_count, 'images available for this query.')

            } catch (err) {
                console.log(err)
            }
        }

    }
})