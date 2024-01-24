import { createBrowserRouter } from 'react-router-dom';
import { Landing } from '../view/pages/Landing';
import { Catalog } from '../view/pages/Catalog';
import { ProductDetails } from '../view/pages/ProductDetails';

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Landing />,
    },
    {
        path: '/catalog',
        element: <Catalog />,
    },
    {
        path: '/catalog/*',
        element: <ProductDetails />,
    },
]);
