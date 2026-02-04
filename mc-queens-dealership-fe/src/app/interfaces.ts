
    // "brand": "toyota",
    // "model": "mr2",
    // "price": 25000,
    // "year": 1984
    // "doors": 3,
    // "fuel_type": "benz",
    // "image_name": "9f81bd4c727447b1f9763f0c25ba8b96.jpg",
    // "description": "is smol is fast",
    // "likes": [],
export interface Car {
    id: number;
    brand: string;
    model: string;
    price: number;
    year: number;
    doors: number;
    fuel_type: string;
    image_name: string;
    description: string;
    likes: Like[];
}

export interface User {
    email: string;
}

export interface Like {
    id: number;
    car_id: number;
    user_id: number;
}
export interface CarsList {
    results: Car[],
    pagination: Pagination
}
    // "count": 2,
    // "page": 1,
    // "pages": 1,
    // "per_page": 24
export interface Pagination {
    count: number;
    page: number;
    pages: number;
    per_page: number;
}

export interface FilterArg {
    name: string;
    value: string;
}