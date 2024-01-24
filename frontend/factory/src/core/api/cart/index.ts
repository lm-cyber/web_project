import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ICartProduct } from './types.ts';

const cartsSlice = createSlice({
    name: 'cart',
    initialState: [] as ICartProduct[],
    reducers: {
        addToCart: (state, action: PayloadAction<ICartProduct>) => {
            const productIndex = state.findIndex((product) => product.id === action.payload.id);

            if (productIndex !== -1) {
                state[productIndex].amount += 1;
            } else {
                state.push({ ...action.payload, amount: 1 });
            }
        },
    },
});

export const { addToCart } = cartsSlice.actions;

export default cartsSlice.reducer;
