const fetchCountries = async() => {
    try {
        const response = await fetch('https://restcountries.com/v3.1/all?fields=name,capital,flags,region')
        const data = response.json()
        return data

    } catch (error) {
        throw new Error('an error occured: ', error)
    }
}

const fetchCountry = async(countryName) => {
    const url = `https://restcountries.com/v3.1/name/${countryName}`
    const response = await fetch(url)
    const data = response.json()
    return data
}

const countryContainer = document.getElementById("country-container")

const displayCountry = async() => {

    const countries = await fetchCountries()
    let html = '';
    countries.forEach(element => {
        html += `
        <div class="country-card">
        <img src="${element.flags.png}" alt="${element.official}">
        <h2>${element.name.official}</h2>
        <p><strong>Capital:</strong> ${element.capital}</p>
        <p><strong>Region:</strong> ${element.region}</p>
    </div>   `
    });
    countryContainer.innerHTML = html
}

const searchBar = document.getElementById("searchBar")
searchBar.addEventListener("input", async() => {
    const searchTerm = searchBar.value.toLowerCase()
    const countries = await fetchCountry(searchTerm)
    let html = '';
    countries.forEach(element => {
        html += `
        <div class="country-card">
        <img src="${element.flags.png}" alt="${element.official}">
        <h2>${element.name.official}</h2>
        <p><strong>Capital:</strong> ${element.capital}</p>
        <p><strong>Region:</strong> ${element.region}</p>
    </div>   `
    });
    countryContainer.innerHTML = html
})


displayCountry()