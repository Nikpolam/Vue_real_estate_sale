<template>
  <v-container>
    <v-form @submit.prevent="onSubmit" ref="form">
      <v-card class="mx-auto mt-6" max-width="800" elevation="4">
        <v-card-title class="text-h5 font-weight-bold primary white--text pa-4">
          Форма регистрации
        </v-card-title>
        
        <v-card-text class="pt-4">
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="firstName"
                :error-messages="errors.firstName"
                label="Имя"
                required
                @input="validateField('firstName')"
                outlined
                dense
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                v-model="lastName"
                :error-messages="errors.lastName"
                label="Фамилия"
                required
                @input="validateField('lastName')"
                outlined
                dense
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field
                v-model="email"
                :error-messages="errors.email"
                label="Email"
                required
                @input="validateField('email')"
                outlined
                dense
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field
                v-model="phone"
                :error-messages="errors.phone"
                label="Телефон"
                required
                @input="validateField('phone')"
                outlined
                dense
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-select
                v-model="serviceType"
                :items="serviceTypes"
                :error-messages="errors.serviceType"
                label="Тип услуги"
                required
                @change="validateField('serviceType')"
                outlined
                dense
              ></v-select>
            </v-col>

            <v-col cols="12">
              <v-textarea
                v-model="message"
                :error-messages="errors.message"
                label="Дополнительная информация"
                @input="validateField('message')"
                outlined
                dense
              ></v-textarea>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            type="submit"
            :loading="loading"
            large
          >
            Отправить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-container>
</template>

<script>
import { defineComponent, ref, reactive } from 'vue'
import { useField, useForm } from 'vee-validate'
import * as yup from 'yup'

export default defineComponent({
  name: 'RegistrationForm',
  
  setup() {
    const loading = ref(false)
    const errors = reactive({})

    const schema = yup.object({
      firstName: yup.string().required('Введите имя'),
      lastName: yup.string().required('Введите фамилию'),
      email: yup.string().required('Введите email').email('Введите корректный email'),
      phone: yup.string().required('Введите номер телефона'),
      serviceType: yup.string().required('Выберите тип услуги'),
      message: yup.string(),
    })

    const { handleSubmit } = useForm({
      validationSchema: schema,
    })

    const serviceTypes = [
      'Регистрация на осмотр квартиры/дома',
      'Регистрация на консультацию',
      'Добавить своё резюме на продажу квартиры/дома',
    ]

    const { value: firstName } = useField('firstName')
    const { value: lastName } = useField('lastName')
    const { value: email } = useField('email')
    const { value: phone } = useField('phone')
    const { value: serviceType } = useField('serviceType')
    const { value: message } = useField('message')

    const validateField = async (fieldName) => {
      try {
        await schema.validateAt(fieldName, {
          firstName: firstName.value,
          lastName: lastName.value,
          email: email.value,
          phone: phone.value,
          serviceType: serviceType.value,
          message: message.value,
        })
        errors[fieldName] = ''
      } catch (err) {
        errors[fieldName] = err.message
      }
    }

    const onSubmit = handleSubmit(async (values) => {
      loading.value = true
      try {
        // Здесь будет логика отправки данных на сервер
        console.log('Form submitted:', values)
        alert('Форма успешно отправлена!')
      } catch (error) {
        console.error('Error submitting form:', error)
        alert('Произошла ошибка при отправке формы')
      } finally {
        loading.value = false
      }
    })

    return {
      firstName,
      lastName,
      email,
      phone,
      serviceType,
      serviceTypes,
      message,
      errors,
      loading,
      validateField,
      onSubmit,
    }
  },
})
</script>

<style scoped>
.v-card {
  border-radius: 8px;
}

.v-card-title {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
</style>
