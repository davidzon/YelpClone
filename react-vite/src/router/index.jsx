import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage/SignupFormPage';
import HomePage from '../components/HomePage/HomePage';
import ExperienceDetailPage from '../components/ExperienceDetailPage/ExperienceDetailPage';
import CreateExperiencePage from '../components/CreateExperiencePage/CreateExperiencePage';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "experiences/:id",
        element: <ExperienceDetailPage />,
      },
      {
        path: "create",
        element: <CreateExperiencePage />,
      }
    ],
  },
]);
