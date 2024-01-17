// Function to fetch product data
async function fetchProducts() {
    try {
        // Make a GET request to the API endpoint
        const response = await fetch('/api/v1/product/');
        
        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const products = await response.json();

        // Get the div where we want to display the products
        const container = document.getElementById('product-container');

        // Clear previous content
        container.innerHTML = '';

        // Iterate over the products and add them to the div
        products.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.innerHTML = `Name: ${product.name}, Description: ${product.description}`;
            container.appendChild(productDiv);
        });
    } catch (error) {
        console.error('There was a problem fetching the product data:', error);
    }
}

// Call the function to fetch and display the products
fetchProducts();
