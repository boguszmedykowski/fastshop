<template>
    <div>
      <h2>Zarejestruj</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="email" placeholder="Email" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Zarejestruj</button>
      </form>
    </div>

  </template>
  
  <script>
  export default {
    name: 'UserRegister',
    data() {
      return {
        email: '',
        password: '',
        errorMessage: '',
        showSnackbar: false,
        snackbarTimeout: null,
      }
    },
    methods: {
      async register() {
        try {
          const response = await this.$axios.post('/users/', {
            email: this.email,
            password: this.password
          });
          console.log(response.data);
          if (response.status === 201) {
            this.$router.push('/UserLogin');
          }
        } catch (error) {
          console.error(error);
          if (error.response && error.response.data) {
            // Zapisz komunikat o błędzie z serwera
            this.errorMessage = error.response.data.error || 'Wystąpił błąd podczas rejestracji.';
          } else {
            // Zapisz ogólny komunikat o błędzie, jeśli odpowiedź serwera nie jest dostępna
            this.errorMessage = 'Wystąpił błąd podczas rejestracji.';
          }
          this.displaySnackbar(); // Wywołaj snackbar z komunikatem o błędzie
        }
      },
      displaySnackbar() {
        this.showSnackbar = true;
        clearTimeout(this.snackbarTimeout); // Czyść poprzedni timeout, jeśli istnieje
        this.snackbarTimeout = setTimeout(() => {
          this.showSnackbar = false;
        }, 3000); // Ustaw czas wyświetlania snackbar na 3 sekundy
      }
    }
  };
  </script>
  

  <style scoped>
div {
  background-color: #f3e0dc; /* jasny, ciepły kolor tła */
  border-radius: 10px;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
}

h2 {
  color: #5a2a27; /* ciemniejszy kolor tekstu */
  font-family: 'Cookie', cursive; /* stylowy font, jeśli dostępny */
}

input[type="text"], input[type="password"] {
  border: 2px solid #5a2a27;
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 5px;
  width: 90%;
}

button {
  background-color: #5a2a27; /* kolor przycisku */
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  padding: 10px 20px;
  text-transform: uppercase;
}

button:hover {
  background-color: #7a3b34; /* kolor przycisku po najechaniu */
}
</style>
  