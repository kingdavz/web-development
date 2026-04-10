document.addEventListener("DOMContentLoaded", () => {
    // 1. Setup variables for IntersectionObserver
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-links a");

    // Configure the observer
    // rootMargin offset ensures the active state changes slightly before the section hits the exact middle
    const observerOptions = {
        root: null,
        rootMargin: "-20% 0px -70% 0px",
        threshold: 0
    };

    // 2. Observer Callback function
    const observerCallback = (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Get the id of the currently intersecting section
                const activeId = entry.target.id;

                // Remove 'active' class from all links
                navLinks.forEach(link => {
                    link.classList.remove("active");

                    // If the href matches the section ID, add the active class
                    if (link.getAttribute("href") === `#${activeId}`) {
                        link.classList.add("active");
                    }
                });
            }
        });
    };

    // 3. Initialize and attach observer
    const observer = new IntersectionObserver(observerCallback, observerOptions);

    sections.forEach(section => {
        if (section.id) { // Only observe sections with IDs
            observer.observe(section);
        }
    });

    // Optional: Mobile menu toggle logic
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinksContainer = document.querySelector('.nav-links');

    menuToggle.addEventListener('click', () => {
        // Simple toggle for mobile nav visibility (requires minor CSS addition to display if built further)
        navLinksContainer.style.display = navLinksContainer.style.display === 'flex' ? 'none' : 'flex';
        navLinksContainer.style.flexDirection = 'column';
        navLinksContainer.style.position = 'absolute';
        navLinksContainer.style.top = '80px';
        navLinksContainer.style.left = '0';
        navLinksContainer.style.width = '100%';
        navLinksContainer.style.backgroundColor = '#0a0a0a';
        navLinksContainer.style.padding = '20px';
    });
});

const typedRoles = ['Frontend Developer', 'React Specialist', 'UI/UX Enthusiast', 'Full Stack Developer'];
let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typedEl = document.getElementById('typed-role');

function typeRole() {
    if (!typedEl) return;
    const current = typedRoles[roleIndex];

    if (isDeleting) {
        typedEl.textContent = current.slice(0, charIndex - 1);
        charIndex--;
    } else {
        typedEl.textContent = current.slice(0, charIndex + 1);
        charIndex++;
    }

    let delay = isDeleting ? 60 : 100;

    if (!isDeleting && charIndex === current.length) {
        delay = 1800;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % typedRoles.length;
        delay = 300;
    }

    setTimeout(typeRole, delay);
}

typeRole();