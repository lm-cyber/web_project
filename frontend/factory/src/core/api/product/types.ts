export interface IImage {
    id: string;
}

export interface IProduct {
    id: number;
    name: string;
    type_of_product_id: number;
    description: string;
    images: IImage[];
}

export interface IProductType {
    id: number;
    name: string;
}
