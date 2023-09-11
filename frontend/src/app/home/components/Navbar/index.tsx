import { AppBar, Box, Toolbar, Typography, Button, ThemeProvider, Container } from "@mui/material";
import { useNavigate } from "react-router-dom";


export default function Navbar({ navTitle }) {

  let navigate = useNavigate();

  const handleClick = (url: string) => {
    navigate(url);
  }

  return(
    <Container>
    <Box sx={{ flexGrow: 1, position: "absolute", width: "100vw", left: 0 }}>
      <AppBar position="static" sx={{ backgroundColor: '#450068'}}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontFamily: "Segoe UI" }}>
            {navTitle}
          </Typography>
          <Button
            size="large"
            variant="text"
            onClick={() => handleClick('/login')}
            sx={{
              color: 'white',
              borderColor: 'white',
              width: '120px',
              marginRight: '10px'
              }}
          >
            LOGIN
          </Button>
          <Button 
            size="large"
            variant="outlined"
            sx={{ color: 'white', borderColor: 'white' }}
            onClick={() => handleClick('/users')}
          >
            ASSINAR
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
    </Container>
  );
}
