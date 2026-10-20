<template>
  <div class="cloud-container">
    <h2>Mi Nube Personal</h2>
    
    <!-- Formulario de subida -->
    <div class="upload-section">
      <input type="file" @change="handleFileUpload" />
      <button @click="submitFile" :disabled="!selectedFile">Subir Archivo</button>
    </div>

    <!-- Lista de archivos almacenados -->
    <div class="file-list">
      <h3>Archivos Compartidos</h3>
      <ul>
        <li v-for="file in files" :key="file.id">
          <span>{{ file.name }}</span>
          <a :href="file.file" target="_blank" download>Descargar / Ver</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const files = ref([]);
const selectedFile = ref(null);

// Obtener la lista de archivos del servidor
const fetchFiles = async () => {
  try {
    const response = await axios.get('https://backend-sumativa.onrender.com/api/files/');
    files.value = response.data;
  } catch (error) {
    console.error("Error obteniendo archivos:", error);
  }
};

// Capturar el archivo seleccionado
const handleFileUpload = (event) => {
  selectedFile.value = event.target.files[0];
};

// Enviar el archivo al servidor Django
const submitFile = async () => {
  if (!selectedFile.value) return;

  const formData = new FormData();
  formData.append('name', selectedFile.value.name);
  formData.append('file', selectedFile.value);

  try {
    await axios.post('https://backend-sumativa.onrender.com/api/files/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    selectedFile.value = null; 
    fetchFiles(); // Refrescar la lista
    alert("Archivo subido exitosamente");
  } catch (error) {
    console.error("Error subiendo el archivo:", error);
  }
};

onMounted(() => {
  fetchFiles();
});
</script>

<style scoped>
.cloud-container {
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}
.upload-section {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.file-list li {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
</style>