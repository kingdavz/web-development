// =====================
// Product Data
// =====================
const products = [
    // Tech
    { name: "Laptop", category: "tech", price: 1200, image: "https://via.placeholder.com/200" },
    { name: "Smartphone", category: "tech", price: 800, image: "https://via.placeholder.com/200" },
    { name: "Headphones", category: "tech", price: 150, image: "https://via.placeholder.com/200" },
    { name: "Smartwatch", category: "tech", price: 250, image: "https://via.placeholder.com/200" },
    { name: "Keyboard", category: "tech", price: 70, image: "https://via.placeholder.com/200" },

    // Fashion
    { name: "T-Shirt", category: "fashion", price: 25, image: "https://via.placeholder.com/200" },
    { name: "Jeans", category: "fashion", price: 60, image: "https://via.placeholder.com/200" },
    { name: "Sneakers", category: "fashion", price: 80, image: "https://via.placeholder.com/200" },
    { name: "Jacket", category: "fashion", price: 120, image: "https://via.placeholder.com/200" },
    { name: "Cap", category: "fashion", price: 20, image: "https://via.placeholder.com/200" },

    // Home
    { name: "Sofa", category: "home", price: 500, image: "https://via.placeholder.com/200" },
    { name: "Lamp", category: "home", price: 40, image: "https://via.placeholder.com/200" },
    { name: "Table", category: "home", price: 150, image: "https://via.placeholder.com/200" },
    { name: "Chair", category: "home", price: 85, image: "https://via.placeholder.com/200" },
    { name: "Curtains", category: "home", price: 60, image: "https://via.placeholder.com/200" }
];

// =====================
// DOM Elements
// =====================
const productList = document.getElementById("productList");
const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");
const minPriceInput = document.getElementById("minPrice");
const maxPriceInput = document.getElementById("maxPrice");
const sortOption = document.getElementById("sortOption");

// =====================
// Display Products
// =====================
function displayProducts(items) {
    productList.innerHTML = "";

    if (items.length === 0) {
        productList.innerHTML = "<p>No products found</p>";
        return;
    }

    items.forEach(product => {
        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>Category: ${product.category}</p>
            <p class="price">$${product.price}</p>
        `;

        productList.appendChild(card);
    });
}

// =====================
// Filter + Sort Logic
// =====================
function filterProducts() {
    const searchText = searchInput.value.toLowerCase();
    const selectedCategory = categoryFilter.value;
    const minPrice = parseFloat(minPriceInput.value) || 0;
    const maxPrice = parseFloat(maxPriceInput.value) || Infinity;

    let filtered = products.filter(product => {
        return (
            product.name.toLowerCase().includes(searchText) &&
            (selectedCategory === "all" || product.category === selectedCategory) &&
            product.price >= minPrice &&
            product.price <= maxPrice
        );
    });

    // Sorting
    if (sortOption.value === "low-high") {
        filtered.sort((a, b) => a.price - b.price);
    } else if (sortOption.value === "high-low") {
        filtered.sort((a, b) => b.price - a.price);
    }

    displayProducts(filtered);
}

// =====================
// Event Listeners
// =====================
searchInput.addEventListener("input", filterProducts);
categoryFilter.addEventListener("change", filterProducts);
minPriceInput.addEventListener("input", filterProducts);
maxPriceInput.addEventListener("input", filterProducts);
sortOption.addEventListener("change", filterProducts);

// =====================
// Initial Load
// =====================
displayProducts(products);