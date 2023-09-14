import React, { useState, useContext } from 'react';
import { Box, Grid, TextField, Button, FormControlLabel, Checkbox, Container, Avatar, Typography } from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


interface formData {
  name: string,
  surname: string,
  email: string,
  passwd: string,
  birthdate: string,
  plan: boolean
}

export default function Subscribe() {
  const [formData, setFormData] = useState<formData>({
    name: '',
    surname: '',
    email: '',
    passwd: '',
    birthdate: '',
    plan: false
  });

let navigate = useNavigate();

const handleClick = (url: string) => {
    navigate(url);
}


  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;

    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8000/users/', formData);

      console.log(formData);
      if (response.status === 201) {
        console.log("Form data submitted");
        setFormData({
          name: '',
          surname: '',
          email: '',
          passwd: '',
          birthdate: '',
          plan: false,
        });
        
        const response_post = await axios.post(`http://localhost:8000/profiles`, {
          nickname: formData.name,
          pg: 18,
          language: 'pt'
        }, {headers: {Authorization: `Bearer ${response.data.id}`}})
        
        navigate('/login');
      } else {
        console.error("Form submission failed");
      }
    } catch (error) {
      console.error('Error: ', error);
    }
  };


  return (
      <Container component="main" maxWidth="xs" sx={{ backgroundColor: "#fff"}}>
        <Box
          sx={{
            borderTop: 20,
            borderBottom: 10,
            borderColor: 'white',
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{
            m:1,
            bgcolor: 'secondary.main'
          }}>
            <LockOutlinedIcon/>
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign Up
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  data-cy='nome'
                  variant='outlined'
                  name="name"
                  label="First Name"
                  value={formData.name}
                  onChange={handleChange}
                  autoFocus
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  data-cy='sobrenome'
                  variant='outlined'
                  id="surname"
                  label="Last Name"
                  name="surname"
                  value={formData.surname}
                  onChange={handleChange}
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  data-cy='email'
                  id="email"
                  label="Email Address"
                  name="email"
                  type='email'
                  value={formData.email}
                  onChange={handleChange}
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  data-cy='data de nascimento'
                  id='birthdate'
                  type='date'
                  name='birthdate'
                  value={formData.birthdate}  
                  onChange={handleChange}
                  fullWidth
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  data-cy='senha'
                  name="passwd"
                  label="Password"
                  type="password"
                  id="password"
                  value={formData.passwd}
                  onChange={handleChange}
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <FormControlLabel
                  control={
                    <Checkbox
                      name="plan"
                      color="primary"
                      checked={formData.plan}
                      onChange={handleChange}
                    />
                  }
                  label="Subscribe to plan"
                />
              </Grid>
            </Grid>
            <Button
              data-cy='criar conta'
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              onClick={() => handleClick("/login")}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Button onClick={() => handleClick("/login")} variant='text' size='small'>
                  Already have an account? Sign in
                </Button> 
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
  );
}
