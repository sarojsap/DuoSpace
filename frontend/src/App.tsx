import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Login from './pages/Login';
import Pairing from './pages/Pairing';
import Chat from './pages/Chat';
import Timeline from './pages/Timeline';
import DailyPrompt from './pages/DailyPrompt';

function App() {
  // We'll replace this with real auth state soon
  const isAuthenticated = !!localStorage.getItem('accessToken');

  return (
    <Router>
      <Routes>
        {/* Public Route */}
        <Route path="/login" element={<Login />} />

        {/* Private Routes wrapped in Mobile Layout */}
        <Route element={<Layout />}>
          <Route path="/pairing" element={<Pairing />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/timeline" element={<Timeline />} />
          <Route path="/prompts" element={<DailyPrompt />} />
        </Route>

        {/* Default Redirect */}
        <Route path="*" element={<Navigate to={isAuthenticated ? "/chat" : "/login"} replace />} />
      </Routes>
    </Router>
  );
}

export default App;