document.addEventListener("DOMContentLoaded", function () {
    const hamburgerButton = document.getElementById("hamburger-button");
    const mobileMenu = document.getElementById("mobile-menu");
    const closeMobileMenuButton = document.getElementById("close-mobile-menu");
    const dynamicMobileMenu = document.getElementById("dynamic-mobile-menu");

    // Populate dynamic mobile menu options
    const mobileMenuOptions = [
        { href: "#Booking", text: "Booking" },
        { href: "#AboutUs", text: "About Us" },
        { href: "#Services", text: "Services" },
        { href: "#Team", text: "Team" },
        { href: "#Products", text: "Products" },
        { href: "#Studio", text: "Studio" },
        { href: "#Testimonials", text: "Testimonials" },
        { href: "#Jobs", text: "Jobs and Vacancies" },
        { href: "#Contact", text: "Contact" },
    ];

    mobileMenuOptions.forEach(option => {
        const link = document.createElement("a");
        link.href = option.href;
        link.className = "hover:opacity-90";
        link.textContent = option.text;
        dynamicMobileMenu.appendChild(link);
    });

    // Toggle mobile menu visibility
    hamburgerButton.addEventListener("click", function () {
        mobileMenu.classList.toggle("hidden");
    });

    // Close mobile menu
    closeMobileMenuButton.addEventListener("click", function () {
        mobileMenu.classList.add("hidden");
    });
});
