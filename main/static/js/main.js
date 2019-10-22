/*	==================================================
	FILE: main.js
	DESC: Custom JS/jQuery
 *	=============================================== */

//Creates a slding nav bar by changing the 'transform' property in .col.middle from 100% to 0%
const navSlide = () => {
	const burger = document.querySelector('.burger');
	const nav = document.querySelector('.col.middle');

	burger.addEventListener('click', () => {
		$(nav).toggleClass("approved");
	});
};

navSlide();
