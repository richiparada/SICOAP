<template>
  <div>
    <h1>Lista de Proveedores</h1>
    <ul>
      <li v-for="proveedor in proveedores" :key="proveedor.id">
        {{ proveedor.nombre }} - {{ proveedor.empresa }} - {{ proveedor.numero_contacto }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      proveedores: []
    };
  },
  created() {
    this.fetchProveedores();
  },
  methods: {
    fetchProveedores() {
      axios.get('http://localhost:8000/api/proveedores/')
        .then(response => {
          this.proveedores = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>