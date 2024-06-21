<script>
  import { onMount } from "svelte";


  let isDragging = false,
    isAutoPlay = false,
    startX,
    startScrollLeft,
    timeoutId;

  let AOS;
  onMount(async () => {
    if (typeof window !== "undefined") {
      const module = await import("aos");
      AOS = module.default;
      AOS.init({
        duration: 1000,
      });
    }
  });
  onMount(() => {
    const wrapper = document.querySelector(".wrapper");
    const carousel = document.querySelector(".carousel");
    const firstCardWidth = carousel.querySelector(".card").offsetWidth;
    const arrowBtns = document.querySelectorAll(".wrapper i");
    const carouselChildrens = [...carousel.children];

    // Get the number of cards that can fit in the carousel at once
    let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);

    // Insert copies of the last few cards to beginning of carousel for infinite scrolling
    carouselChildrens
      .slice(-cardPerView)
      .reverse()
      .forEach((card) => {
        carousel.insertAdjacentHTML("afterbegin", card.outerHTML);
      });

    // Insert copies of the first few cards to end of carousel for infinite scrolling
    carouselChildrens.slice(0, cardPerView).forEach((card) => {
      carousel.insertAdjacentHTML("beforeend", card.outerHTML);
    });

    // Scroll the carousel at appropriate postition to hide first few duplicate cards on Firefox
    carousel.classList.add("no-transition");
    carousel.scrollLeft = carousel.offsetWidth;
    carousel.classList.remove("no-transition");

    // Add event listeners for the arrow buttons to scroll the carousel left and right
    arrowBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        carousel.scrollLeft +=
          btn.id == "left" ? -firstCardWidth : firstCardWidth;
      });
    });

    const dragStart = (e) => {
  isDragging = true;
  carousel.classList.add("dragging");
  // Records the initial cursor and scroll position of the carousel
  startX = e.pageX || e.touches[0].pageX;
  startScrollLeft = carousel.scrollLeft;
  e.preventDefault(); // Prevent default behavior
};

const dragging = (e) => {
  if (!isDragging) return; // if isDragging is false return from here
  // Updates the scroll position of the carousel based on the cursor movement
  const x = e.pageX || e.touches[0].pageX;
  carousel.scrollLeft = startScrollLeft - (x - startX);
  e.preventDefault(); // Prevent default behavior
};

const dragStop = (e) => {
  isDragging = false;
  carousel.classList.remove("dragging");
  e.preventDefault(); // Prevent default behavior
};
    const infiniteScroll = () => {
      // If the carousel is at the beginning, scroll to the end
      if (carousel.scrollLeft === 0) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.scrollWidth - 2 * carousel.offsetWidth;
        carousel.classList.remove("no-transition");
      }
      // If the carousel is at the end, scroll to the beginning
      else if (
        Math.ceil(carousel.scrollLeft) ===
        carousel.scrollWidth - carousel.offsetWidth
      ) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.offsetWidth;
        carousel.classList.remove("no-transition");
      }
      // Clear existing timeout & start autoplay if mouse is not hovering over carousel
      clearTimeout(timeoutId);
      if (!wrapper.matches(":hover")) autoPlay();
    };

    const autoPlay = () => {
      if (window.innerWidth < 800 || !isAutoPlay) return; // Return if window is smaller than 800 or isAutoPlay is false
      // Autoplay the carousel after every 2500 ms
      timeoutId = setTimeout(
        () => (carousel.scrollLeft += firstCardWidth),
        2500
      );
    };

    autoPlay();
    carousel.addEventListener("mousedown", dragStart);
    carousel.addEventListener("mousemove", dragging);
    document.addEventListener("mouseup", dragStop);
    carousel.addEventListener("scroll", infiniteScroll);
    wrapper.addEventListener("mouseenter", () => clearTimeout(timeoutId));
    wrapper.addEventListener("mouseleave", autoPlay);

    document.addEventListener("DOMContentLoaded", function () {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("slide-fade-in");
          } else {
            entry.target.classList.remove("slide-fade-in");
          }
        });
      });

      observer.observe(document.querySelector(".containerSectionTop"));
    });
  });
  onMount(() => {
    const wrapper = document.querySelector(".faqWrapper");
    const carousel = document.querySelector(".faqCarousel");
    const firstCardWidth = carousel.querySelector(".card").offsetWidth;
    const arrowBtns = document.querySelectorAll(".faqWrapper i");
    const carouselChildrens = [...carousel.children];

    // Get the number of cards that can fit in the carousel at once
    let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);

    // Insert copies of the last few cards to beginning of carousel for infinite scrolling
    carouselChildrens
      .slice(-cardPerView)
      .reverse()
      .forEach((card) => {
        carousel.insertAdjacentHTML("afterbegin", card.outerHTML);
      });

    // Insert copies of the first few cards to end of carousel for infinite scrolling
    carouselChildrens.slice(0, cardPerView).forEach((card) => {
      carousel.insertAdjacentHTML("beforeend", card.outerHTML);
    });

    // Scroll the carousel at appropriate postition to hide first few duplicate cards on Firefox
    carousel.classList.add("no-transition");
    carousel.scrollLeft = carousel.offsetWidth;
    carousel.classList.remove("no-transition");

    // Add event listeners for the arrow buttons to scroll the carousel left and right
    arrowBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        carousel.scrollLeft +=
          btn.id == "left" ? -firstCardWidth : firstCardWidth;
      });
    });

    const dragStart = (e) => {
      isDragging = true;
      carousel.classList.add("dragging");
      // Records the initial cursor and scroll position of the carousel
      startX = e.pageX;
      startScrollLeft = carousel.scrollLeft;
    };

    const dragging = (e) => {
      if (!isDragging) return; // if isDragging is false return from here
      // Updates the scroll position of the carousel based on the cursor movement
      carousel.scrollLeft = startScrollLeft - (e.pageX - startX);
    };

    const dragStop = () => {
      isDragging = false;
      carousel.classList.remove("dragging");
    };

    const infiniteScroll = () => {
      // If the carousel is at the beginning, scroll to the end
      if (carousel.scrollLeft === 0) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.scrollWidth - 2 * carousel.offsetWidth;
        carousel.classList.remove("no-transition");
      }
      // If the carousel is at the end, scroll to the beginning
      else if (
        Math.ceil(carousel.scrollLeft) ===
        carousel.scrollWidth - carousel.offsetWidth
      ) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.offsetWidth;
        carousel.classList.remove("no-transition");
      }
      // Clear existing timeout & start autoplay if mouse is not hovering over carousel
      clearTimeout(timeoutId);
      if (!wrapper.matches(":hover")) autoPlay();
    };

    const autoPlay = () => {
      if (window.innerWidth < 800 || !isAutoPlay) return; // Return if window is smaller than 800 or isAutoPlay is false
      // Autoplay the carousel after every 2500 ms
      timeoutId = setTimeout(
        () => (carousel.scrollLeft += firstCardWidth),
        2500
      );
    };

    autoPlay();
    carousel.addEventListener("mousedown", dragStart);
    carousel.addEventListener("mousemove", dragging);
    document.addEventListener("mouseup", dragStop);
    carousel.addEventListener("scroll", infiniteScroll);
    wrapper.addEventListener("mouseenter", () => clearTimeout(timeoutId));
    wrapper.addEventListener("mouseleave", autoPlay);

    document.addEventListener("DOMContentLoaded", function () {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("slide-fade-in");
          } else {
            entry.target.classList.remove("slide-fade-in");
          }
        });
      });

      observer.observe(document.querySelector(".containerSectionTop"));
    });
  });

  
  onMount(() => {
    // Open the first accordion item by default
    const firstAccordionHeader = document.querySelector('.accordion-header');
    const firstAccordionContent = firstAccordionHeader.nextElementSibling;
    firstAccordionHeader.classList.add('active');
    firstAccordionHeader.style.color = '#21A5C3'; // Change font color for the first active header
    firstAccordionContent.style.maxHeight = firstAccordionContent.scrollHeight + 'px';
    firstAccordionContent.style.opacity = '1';
    firstAccordionContent.classList.add('active');

    const firstIcon = firstAccordionHeader.querySelector('lord-icon');
    firstIcon.src = "https://cdn.lordicon.com/ternnbni.json";
    firstIcon.setAttribute('trigger', 'hover');
    firstIcon.setAttribute('colors', 'primary:#4FE1F9'); // Active color
    firstIcon.setAttribute('style', 'width:50px;height:50px');

    document.querySelectorAll('.accordion-header').forEach((item) => {
      item.addEventListener('click', () => {
        const content = item.nextElementSibling;

        if (content.classList.contains('active')) {
          content.style.maxHeight = '0';
          content.style.opacity = '0';
          content.classList.remove('active');
          item.classList.remove('active');
          item.style.color = ''; // Reset font color
          const icon = item.querySelector('lord-icon');
          icon.src = "https://cdn.lordicon.com/xcrjfuzb.json";
          icon.setAttribute('trigger', 'hover');
          icon.setAttribute('colors', 'primary:#767676');
          icon.setAttribute('style', 'width:50px;height:50px');
        } else {
          document.querySelectorAll('.accordion-content').forEach(content => {
            content.style.maxHeight = '0';
            content.style.opacity = '0';
            content.classList.remove('active');
          });

          document.querySelectorAll('.accordion-header').forEach(header => {
            header.classList.remove('active');
            header.style.color = ''; // Reset font color
            const headerIcon = header.querySelector('lord-icon');
            headerIcon.src = "https://cdn.lordicon.com/xcrjfuzb.json";
            headerIcon.setAttribute('trigger', 'hover');
            headerIcon.setAttribute('colors', 'primary:#767676');
            headerIcon.setAttribute('style', 'width:50px;height:50px');
            headerIcon.style.display = ''; // Reset display
          });

          content.style.maxHeight = content.scrollHeight + 'px';
          content.style.opacity = '1';
          content.classList.remove('active');
          content.classList.add('active');
          item.classList.add('active');
          item.style.color = '#21A5C3'; // Change font color for active header
          const icon = item.querySelector('lord-icon');
          icon.src = "https://cdn.lordicon.com/ternnbni.json";
          icon.setAttribute('trigger', 'hover');
          icon.setAttribute('colors', 'primary:#4FE1F9'); // Active color
          icon.setAttribute('style', 'width:50px;height:50px;'); // Active size
          icon.style.display = 'block'; // Ensure display is block for the active one
        }
      });
    });
  });


</script>

<main>
  <div class="gridBrandImage">
    <img class="brandImage" src="../svg/plane_sky.svg" alt="photo_brand" />
  </div>
  <header class="landingPage">
    <div class="headerContent">
      <div class="bgImage">
        <img src="../svg/hexaMotif.svg" alt="bgImage" />
      </div>
      <div class="headerText">
        <div class="brandName text-primary fontSecondary">Envoyage</div>
        <div class="brandSlogan text-darkPrimary fs-2 fontSecondary">
          gagnez de l’argent tout en voyageant
        </div>
        <div class="headerButtons">
          <button class=""> 
            <a href="/sign-up" class="">Transportez & Gagnez</a>
          </button>
         
        </div>
      </div>
      <div class="logo">
        <img class="logo_envoyage" src="../svg/logo_envoyage.svg" alt="logo" />
      </div>
      <div class="w-50"></div>
    </div>
  </header>
  <section>
    <div class="about">
      <div class="aboutTitle text-primary fs-1 fw-bold fontSecondary" data-aos="fade-down">
        Envoyage ?
      </div>
      <div class="aboutSectionsContainer">
        <div class="containerSectionTop">
          <div class="aboutSection aboutSectionType1" data-aos="fade-up">
            <div
              class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
            >
              Qu'est ce qu'Envoyage ?
            </div>
            <div class="aboutSectionText fs-5 text-basic fontPrimary">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur? Accusantium sapiente tempora fugit
              corporis, laboriosam laudantium? Similique, ratione.
            </div>
          </div>
          <div
            class=""
            data-aos="fade-down-left"
            data-aos-duration="2000"
            data-aos-delay="200"
          >
            <img class="planeImage" src="../svg/plane.svg" alt="plane" />
          </div>
        </div>
        <div class="containerSectionMiddle">
          <div
            class="aboutSectionHexagonLeft"
            data-aos="fade-right"
            data-aos-duration="2000"
            data-aos-delay="500"
          >
            <img
              class="aboutBorderHexaLeft"
              src="../svg/half_hexa_rightpart.svg"
              alt="half_hexa_rightpart"
            />
          </div>
          <div class="aboutSection aboutSectionType2" data-aos="fade-up">
            <div
              class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
            >
              Quel est notre but ?
            </div>
            <div class="aboutSectionText fs-5 text-basic fontPrimary">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur? Accusantium sapiente tempora fugit
              corporis, laboriosam laudantium? Similique, ratione.
            </div>
          </div>
        </div>
        <div class="containerSectionBottom">
          <div class="aboutSection aboutSectionType1" data-aos="fade-up">
            <div
              class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
            >
              Pourquoi Envoyage ?
            </div>
            <div class="aboutSectionText fs-5 text-basic fontPrimary">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur? Accusantium sapiente tempora fugit
              corporis, laboriosam laudantium? Similique, ratione.
            </div>
          </div>
          <div
            class="aboutSectionHexagonRight"
            data-aos="fade-left"
            data-aos-duration="2000"
            data-aos-delay="500"
          >
            <img
              class="aboutBorderHexaRight"
              src="../svg/half_hexa_rightpart.svg"
              alt="half_hexa_leftpart"
            />
          </div>
        </div>
      </div>

      <div class="accordion fontSecondary">
        <div class="accordion-item">
          <div class="accordion-header">
            Qu'est ce qu'Envoyage ?
            <lord-icon
              src="https://cdn.lordicon.com/xcrjfuzb.json"
              trigger="hover"
              colors="primary:#767676"
              style="width:50px;height: 50px">
            </lord-icon>
          </div>
          <div class="accordion-content text-basic">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur.</p>
          </div>
        </div>
        <div class="accordion-item">
          <div class="accordion-header">
            Quel est notre but ?
            <lord-icon
              src="https://cdn.lordicon.com/xcrjfuzb.json"
              trigger="hover"
              colors="primary:#767676"
              style="width:50px;height: 50px">
            </lord-icon>
          </div>
          <div class="accordion-content text-basic">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur.</p>
          </div>
        </div>
        <div class="accordion-item">
          <div class="accordion-header">
            Pourquoi Envoyage ?
            <lord-icon
              src="https://cdn.lordicon.com/xcrjfuzb.json"
              trigger="hover"
              colors="primary:#767676"
              style="width:50px;height: 50px">
            </lord-icon>
          </div>
          <div class="accordion-content text-basic">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="steps stepsPart1">
      <div class="arrow arrowAboutSteps" data-aos="fade-down">
        <svg
          class="arrowSVG"
          fill="#21A5C3"
          height="347"
          viewBox="0 0 198 347"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M191.36 137.224L197.302 138.06L191.36 137.224ZM30.402 346.498C27.3654 347.825 23.8283 346.439 22.5017 343.402L0.883889 293.918C-0.44269 290.881 0.943544 287.344 3.98013 286.018C7.01671 284.691 10.5538 286.077 11.8803 289.114L31.0962 333.1L75.082 313.884C78.1186 312.557 81.6556 313.944 82.9822 316.98C84.3088 320.017 82.9226 323.554 79.886 324.88L30.402 346.498ZM54.2748 0.140731C56.056 3.42689 58.2611 6.59445 60.8525 9.6692L51.6767 17.4025C48.6316 13.7894 45.9442 9.95333 43.725 5.85927L54.2748 0.140731ZM78.7967 25.8217C85.2231 30.4903 92.3572 34.9216 99.9037 39.2694L93.9132 49.6671C86.1706 45.2064 78.6406 40.5405 71.7438 35.5304L78.7967 25.8217ZM122.232 51.5547C129.839 55.6513 137.517 59.7965 144.862 64.0812L138.816 74.4466C131.674 70.2806 124.171 66.2285 116.542 62.1201L122.232 51.5547ZM166.921 78.4814C174.47 84.1764 181.242 90.4144 186.514 97.4448L176.914 104.644C172.53 98.7987 166.68 93.3313 159.694 88.0609L166.921 78.4814ZM197.485 123.684C198.049 128.278 198.005 133.066 197.302 138.06L185.419 136.388C185.983 132.383 186.005 128.65 185.575 125.147L197.485 123.684ZM197.302 138.06C196.626 142.863 195.693 147.461 194.524 151.876L182.924 148.803C183.969 144.858 184.808 140.727 185.419 136.388L197.302 138.06ZM183.935 177.922C179.299 186.156 173.757 193.617 167.596 200.559L158.621 192.594C164.319 186.174 169.331 179.401 173.479 172.034L183.935 177.922ZM147.942 219.734C141.234 225.558 134.171 231.182 127.004 236.78L119.618 227.323C126.745 221.756 133.609 216.286 140.074 210.673L147.942 219.734ZM106.025 253.191C99.2238 258.623 92.4752 264.221 85.9115 270.17L77.8534 261.278C84.6674 255.103 91.6246 249.334 98.5369 243.814L106.025 253.191ZM67.4889 288.597C61.8516 294.902 56.5018 301.647 51.5558 308.967L41.6126 302.249C46.8934 294.433 52.5845 287.264 58.5432 280.599L67.4889 288.597ZM38.7419 331.319C36.9191 335.127 35.1968 339.08 33.5863 343.189L22.4137 338.811C24.1311 334.429 25.9698 330.208 27.918 326.138L38.7419 331.319Z"
          />
        </svg>
      </div>
      <div class="step01 step">
        <div class="stepTop step01Top">
          <div class="stepContent">
            <div class="stepTitle text-basic fw-bold fs-2 fontSecondary">
              <div
                class="stepNumber fontSecondary"
                data-aos="fade-up-right"
                data-aos-delay="100"
              >
                01'
              </div>
              <div class="text fw-bold" data-aos="fade-up" data-aos-delay="550">
                Trouvez votre
                <div
                  class="highlight bg-primary text-white"
                  data-aos="flip-up"
                  data-aos-delay="1000"
                >
                  <p class="m-0" data-aos="flip-down" data-aos-delay="1500">
                    expéditeur
                  </p>
                </div>
              </div>
            </div>
            <div
              class="stepText fs-5 fontPrimary"
              data-aos="fade-up"
              data-aos-delay="560"
            >
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
              culpa eius div dolorem iusto consectetur dolore eum voluptates
              aliquid voluptatem cum amet quaerat commodi et libero esse
              excepturi laudantium nesciunt.
            </div>
          </div>
          <div data-aos="fade-left" data-aos-delay="560">
            <img
              class="stepImage"
              src="../svg/deliveryHome.svg"
              alt="delivery"
            />
          </div>
        </div>
        <div class="stepAds">
          <div
            class="steptitle text-secondary fw-bold fs-2 fontSecondary"
            data-aos="fade-up"
            data-aos-delay="600"
          >
            Quelques annonces
          </div>
        </div>
      </div>
      <div class="wrapper" data-aos="fade" data-aos-delay="650">
        <i id="left" class="fa-solid fa-angle-left text-darkSecondary">&lt</i>
        <div class="carousel fontSecondary">
          <div class="col">
            <div href="" class="card h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Amine Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #4FE1F9;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary">
                  last updated 3 mins ago
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Nassim Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #4FE1F9;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary">
                  last updated 3 mins ago
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Islem Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #4FE1F9;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary">
                  last updated 3 mins ago
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Wassim Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #4FE1F9;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary">
                  last updated 3 mins ago
                </div>
              </div>
            </div>
          </div>
        </div>
        <i id="right" class="fa-solid fa-angle-right text-darkSecondary">&gt</i>
      </div>
      <div class="step01 step">
        <div class="stepAds">
          <div
            class="stepText fs-5 fontPrimary"
            data-aos="fade-up"
            data-aos-delay="550"
          >
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit
            officia, quaerat commodi culpa id fugiat div laudantium tenetur
            doloremque repellat itaque nemo tempora numquam velit impedit minus
            similique doloribus voluptas.
          </div>
          <div class="" data-aos="flip-up" data-aos-delay="700">
            <button
              class="stepButton bg-primary text-white highlight fs-5 fontSecondary"
            >
              Rechercher
            </button>
          </div>
        </div>
      </div>
      <div class="transition">
        <div class="arrow arrowTransitionSteps" data-aos="fade-down">
          <svg
            class="arrowSVG"
            fill="#efefef"
            height="347"
            viewBox="0 0 198 347"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M191.36 137.224L197.302 138.06L191.36 137.224ZM30.402 346.498C27.3654 347.825 23.8283 346.439 22.5017 343.402L0.883889 293.918C-0.44269 290.881 0.943544 287.344 3.98013 286.018C7.01671 284.691 10.5538 286.077 11.8803 289.114L31.0962 333.1L75.082 313.884C78.1186 312.557 81.6556 313.944 82.9822 316.98C84.3088 320.017 82.9226 323.554 79.886 324.88L30.402 346.498ZM54.2748 0.140731C56.056 3.42689 58.2611 6.59445 60.8525 9.6692L51.6767 17.4025C48.6316 13.7894 45.9442 9.95333 43.725 5.85927L54.2748 0.140731ZM78.7967 25.8217C85.2231 30.4903 92.3572 34.9216 99.9037 39.2694L93.9132 49.6671C86.1706 45.2064 78.6406 40.5405 71.7438 35.5304L78.7967 25.8217ZM122.232 51.5547C129.839 55.6513 137.517 59.7965 144.862 64.0812L138.816 74.4466C131.674 70.2806 124.171 66.2285 116.542 62.1201L122.232 51.5547ZM166.921 78.4814C174.47 84.1764 181.242 90.4144 186.514 97.4448L176.914 104.644C172.53 98.7987 166.68 93.3313 159.694 88.0609L166.921 78.4814ZM197.485 123.684C198.049 128.278 198.005 133.066 197.302 138.06L185.419 136.388C185.983 132.383 186.005 128.65 185.575 125.147L197.485 123.684ZM197.302 138.06C196.626 142.863 195.693 147.461 194.524 151.876L182.924 148.803C183.969 144.858 184.808 140.727 185.419 136.388L197.302 138.06ZM183.935 177.922C179.299 186.156 173.757 193.617 167.596 200.559L158.621 192.594C164.319 186.174 169.331 179.401 173.479 172.034L183.935 177.922ZM147.942 219.734C141.234 225.558 134.171 231.182 127.004 236.78L119.618 227.323C126.745 221.756 133.609 216.286 140.074 210.673L147.942 219.734ZM106.025 253.191C99.2238 258.623 92.4752 264.221 85.9115 270.17L77.8534 261.278C84.6674 255.103 91.6246 249.334 98.5369 243.814L106.025 253.191ZM67.4889 288.597C61.8516 294.902 56.5018 301.647 51.5558 308.967L41.6126 302.249C46.8934 294.433 52.5845 287.264 58.5432 280.599L67.4889 288.597ZM38.7419 331.319C36.9191 335.127 35.1968 339.08 33.5863 343.189L22.4137 338.811C24.1311 334.429 25.9698 330.208 27.918 326.138L38.7419 331.319Z"
            />
          </svg>
        </div>
        <div class="groupTransition" data-aos="fade-up">
          <img
            class="transition"
            src="../svg/transition01.svg"
            alt="transition"
          />
          <div class="separationLine"></div>
        </div>
      </div>

      <div class="step02 step">
        <div class="stepTop step02Top">
          <div class="stepContent">
            <div class="stepTitle text-basic fw-bold fs-2 fontSecondary">
              <div
                class="stepNumber fontSecondary"
                data-aos="fade-up-right"
                data-aos-delay="100"
              >
                02'
              </div>
              <div class="text fw-bold" data-aos="fade-up" data-aos-delay="550">
                Remettez lui votre
             
              </div>
              <div
              class="highlight bg-primary text-white"
              data-aos="flip-up"
              data-aos-delay="1000"
            >
              <p class="m-0" data-aos="flip-down" data-aos-delay="1500">
                paquet
              </p>
            </div>
            </div>
            <div
              class="stepText fs-5 fontPrimary"
              data-aos="fade-up"
              data-aos-delay="560"
            >
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
              culpa eius div dolorem iusto consectetur dolore eum voluptates
              aliquid voluptatem cum amet quaerat commodi et libero esse
              excepturi laudantium nesciunt.
            </div>
          </div>
          <div
            class="parentHexaSVGWhite"
            data-aos="fade-left"
            data-aos-delay="560"
          >
            <img
              class="stepImage HexaSVGWhite"
              src="../svg/Hexa_White.svg"
              alt="delivery"
            />
          </div>
        </div>
        <div class="arrow arrowStep2Step3" data-aos="fade-down">
          <svg
            class="arrowSVG"
            fill="#1C1D20"
            height="347"
            viewBox="0 0 198 347"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M191.36 137.224L197.302 138.06L191.36 137.224ZM30.402 346.498C27.3654 347.825 23.8283 346.439 22.5017 343.402L0.883889 293.918C-0.44269 290.881 0.943544 287.344 3.98013 286.018C7.01671 284.691 10.5538 286.077 11.8803 289.114L31.0962 333.1L75.082 313.884C78.1186 312.557 81.6556 313.944 82.9822 316.98C84.3088 320.017 82.9226 323.554 79.886 324.88L30.402 346.498ZM54.2748 0.140731C56.056 3.42689 58.2611 6.59445 60.8525 9.6692L51.6767 17.4025C48.6316 13.7894 45.9442 9.95333 43.725 5.85927L54.2748 0.140731ZM78.7967 25.8217C85.2231 30.4903 92.3572 34.9216 99.9037 39.2694L93.9132 49.6671C86.1706 45.2064 78.6406 40.5405 71.7438 35.5304L78.7967 25.8217ZM122.232 51.5547C129.839 55.6513 137.517 59.7965 144.862 64.0812L138.816 74.4466C131.674 70.2806 124.171 66.2285 116.542 62.1201L122.232 51.5547ZM166.921 78.4814C174.47 84.1764 181.242 90.4144 186.514 97.4448L176.914 104.644C172.53 98.7987 166.68 93.3313 159.694 88.0609L166.921 78.4814ZM197.485 123.684C198.049 128.278 198.005 133.066 197.302 138.06L185.419 136.388C185.983 132.383 186.005 128.65 185.575 125.147L197.485 123.684ZM197.302 138.06C196.626 142.863 195.693 147.461 194.524 151.876L182.924 148.803C183.969 144.858 184.808 140.727 185.419 136.388L197.302 138.06ZM183.935 177.922C179.299 186.156 173.757 193.617 167.596 200.559L158.621 192.594C164.319 186.174 169.331 179.401 173.479 172.034L183.935 177.922ZM147.942 219.734C141.234 225.558 134.171 231.182 127.004 236.78L119.618 227.323C126.745 221.756 133.609 216.286 140.074 210.673L147.942 219.734ZM106.025 253.191C99.2238 258.623 92.4752 264.221 85.9115 270.17L77.8534 261.278C84.6674 255.103 91.6246 249.334 98.5369 243.814L106.025 253.191ZM67.4889 288.597C61.8516 294.902 56.5018 301.647 51.5558 308.967L41.6126 302.249C46.8934 294.433 52.5845 287.264 58.5432 280.599L67.4889 288.597ZM38.7419 331.319C36.9191 335.127 35.1968 339.08 33.5863 343.189L22.4137 338.811C24.1311 334.429 25.9698 330.208 27.918 326.138L38.7419 331.319Z"
            />
          </svg>
        </div>
      </div>

      <div class="steps stepsPart2">
        <div class="step03 step">
          <div class="stepTop step03Top">
            <div class="stepContent">
              <div class="stepTitle text-basic fw-bold fs-2 fontSecondary">
                <div
                  class="stepNumber fontSecondary"
                  data-aos="fade-up-right"
                  data-aos-delay="100"
                >
                  03'
                </div>
                <div
                  class="text fw-bold"
                  data-aos="fade-up"
                  data-aos-delay="550"
                >
                  Récupérez le de l'
               
                </div>
                   <div
                    class="reverseHighlight text-white"
                    data-aos="flip-up"
                    data-aos-delay="1000"
                  >
                    <p class="m-0" data-aos="flip-down" data-aos-delay="1500">
                      autre coté
                    </p>
                  </div>
              </div>
              <div
                class="stepText fs-5 fontPrimary"
                data-aos="fade-up"
                data-aos-delay="560"
              >
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
                culpa eius div dolorem iusto consectetur dolore eum voluptates
                aliquid voluptatem cum amet quaerat commodi et libero esse
                excepturi laudantium nesciunt.
              </div>
            </div>
            <div
              class="parentHexaSVGBlue"
              data-aos="fade-left"
              data-aos-delay="560"
            >
              <img
                class="stepImage HexaSVGBlue"
                src="../svg/Hexa_Blue.svg"
                alt="delivery"
              />
            </div>
          </div>
        </div>
        
      </div>
      <div class="arrow arrowStep3Step4" data-aos="fade-down">
        <svg 
        class="arrowSVG"
        fill="#1C1D20" height="347" viewBox="0 0 198 347" xmlns="http://www.w3.org/2000/svg">
          <path d="M191.36 137.224L197.302 138.06L191.36 137.224ZM30.402 346.498C27.3654 347.825 23.8283 346.439 22.5017 343.402L0.883889 293.918C-0.44269 290.881 0.943544 287.344 3.98013 286.018C7.01671 284.691 10.5538 286.077 11.8803 289.114L31.0962 333.1L75.082 313.884C78.1186 312.557 81.6556 313.944 82.9822 316.98C84.3088 320.017 82.9226 323.554 79.886 324.88L30.402 346.498ZM54.2748 0.140731C56.056 3.42689 58.2611 6.59445 60.8525 9.6692L51.6767 17.4025C48.6316 13.7894 45.9442 9.95333 43.725 5.85927L54.2748 0.140731ZM78.7967 25.8217C85.2231 30.4903 92.3572 34.9216 99.9037 39.2694L93.9132 49.6671C86.1706 45.2064 78.6406 40.5405 71.7438 35.5304L78.7967 25.8217ZM122.232 51.5547C129.839 55.6513 137.517 59.7965 144.862 64.0812L138.816 74.4466C131.674 70.2806 124.171 66.2285 116.542 62.1201L122.232 51.5547ZM166.921 78.4814C174.47 84.1764 181.242 90.4144 186.514 97.4448L176.914 104.644C172.53 98.7987 166.68 93.3313 159.694 88.0609L166.921 78.4814ZM197.485 123.684C198.049 128.278 198.005 133.066 197.302 138.06L185.419 136.388C185.983 132.383 186.005 128.65 185.575 125.147L197.485 123.684ZM197.302 138.06C196.626 142.863 195.693 147.461 194.524 151.876L182.924 148.803C183.969 144.858 184.808 140.727 185.419 136.388L197.302 138.06ZM183.935 177.922C179.299 186.156 173.757 193.617 167.596 200.559L158.621 192.594C164.319 186.174 169.331 179.401 173.479 172.034L183.935 177.922ZM147.942 219.734C141.234 225.558 134.171 231.182 127.004 236.78L119.618 227.323C126.745 221.756 133.609 216.286 140.074 210.673L147.942 219.734ZM106.025 253.191C99.2238 258.623 92.4752 264.221 85.9115 270.17L77.8534 261.278C84.6674 255.103 91.6246 249.334 98.5369 243.814L106.025 253.191ZM67.4889 288.597C61.8516 294.902 56.5018 301.647 51.5558 308.967L41.6126 302.249C46.8934 294.433 52.5845 287.264 58.5432 280.599L67.4889 288.597ZM38.7419 331.319C36.9191 335.127 35.1968 339.08 33.5863 343.189L22.4137 338.811C24.1311 334.429 25.9698 330.208 27.918 326.138L38.7419 331.319Z"/>
          </svg>
      </div>
      <div class="steps stepsPart3">
        <img class="backgroundImageStep03" src="../svg/background3-4.svg" alt="" />

        <div class="headerStep fs-1 text-primary fontSecondary" data-aos="fade-down" data-aos-delay="200">
          Où alors ...
        </div>
        <div class="step04 step">
         
          <div class="stepTop step04Top">
            <div class="stepContent">
              <div class="stepTitle text-basic fw-bold fs-2 fontSecondary">
                <div
                  class="stepNumber fontSecondary"
                  data-aos="fade-up-right"
                  data-aos-delay="100"
                >
                  00'
                </div>
                <div
                  class="text fw-bold"
                  data-aos="fade-up"
                  data-aos-delay="550"
                 >
                  Devenez vous-même
                  
                
                </div>
                <div
                class="highlight bg-primary text-white"
                data-aos="flip-up"
                data-aos-delay="1000"
              >
                <p class="m-0" data-aos="flip-down" data-aos-delay="1500">
                  expéditeur
                </p>
              </div>
              
              <div class="" data-aos="zoom-out-down"
              data-aos-delay="1550">!</div>
              </div>
              <div
                class="stepText fs-5 fontPrimary"
                data-aos="fade-up"
                data-aos-delay="560"
              >
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
                culpa eius div dolorem iusto consectetur dolore eum voluptates
                aliquid voluptatem cum amet quaerat commodi et libero esse
                excepturi laudantium nesciunt.
              </div>
            </div>
            
            <!-- <div
              class="parentHexaSVGBlue"
              data-aos="fade-left"
              data-aos-delay="560"
            >
              <img
                class="stepImage HexaSVGBlue"
                src="../svg/Hexa_Blue.svg"
                alt="delivery"
              />
            </div> -->
            <div class="stepAds step04btn">
              <div class="" data-aos="flip-up" data-aos-delay="700">
                <button
                  class="stepButton bg-primary text-white highlight fs-5 fontSecondary"
                >
                  Devenir expéditeur
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="faq bg-basic">
        <div class="faqContent fs-1">
          <div class="faqText fontSecondary text-white" data-aos="zoom-out-down" data-aos-delay="350">
            <div class="part1TextFaq text-light">
              Questions
            </div>
            fréquemment posées
          </div>
        </div>
        <div class="faqScroller">
          <div class="wrapper faqWrapper" data-aos="fade" data-aos-delay="650">
            <div class="carousel faqCarousel">
              <div class="card col">
                <div class="cardContent">
                  <div class="cardNumber text-white fontSecondary">
                    #1
                  </div>
                  <div class="cardFaq">
                    <div class="cardTitle fs-2 text-light fontSecondary">
                      lorem ipsum dolor sit amet
                    </div>
                    <div class="cardText fs-4 text-basic fontSecondary">
                      Lorem ipsum dolor sit amet consectetur adipisicing elit.
                      Fugit officia, quaerat commodi culpa id fugiat div laudant
                    </div>
                  </div>
                </div>
              </div>
              <div class="card col">
                <div class="cardContent">
                  <div class="cardNumber text-white fontSecondary">
                    #2
                  </div>
                  <div class="cardFaq">
                    <div class="cardTitle fs-2 text-light fontSecondary">
                      lorem ipsum dolor sit amet
                    </div>
                    <div class="cardText fs-4 text-basic fontSecondary">
                      Lorem ipsum dolor sit amet consectetur adipisicing elit.
                      Fugit officia, quaerat commodi culpa id fugiat div laudant
                    </div>
                  </div>
                </div>
              </div>
              <div class="card col">
                <div class="cardContent">
                  <div class="cardNumber text-white fontSecondary">
                    #3
                  </div>
                  <div class="cardFaq">
                    <div class="cardTitle fs-2 text-light fontSecondary">
                      lorem ipsum dolor sit amet
                    </div>
                    <div class="cardText fs-4 text-basic fontSecondary">
                      Lorem ipsum dolor sit amet consectetur adipisicing elit.
                      Fugit officia, quaerat commodi culpa id fugiat div laudant
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="separationFooterStep04"></div>
    </div>
  </section>
</main>

<style>
  @import './responsive.css';
  @import './responsive_fp.css';
  main {
  overflow-x: hidden;
}

section {
  background-color: white;
}

.landingPage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100vh;
  width: 100%;
  position: relative;
}

.bgImage {
  position: absolute;
  left: -10%;
  width: 110%;
  opacity: 15%;
  z-index: -1;
}

.bgImage::after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to top,
    rgba(255, 255, 255, 1) 5%,
    rgba(255, 255, 255, 0) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  pointer-events: none;
}

.headerContent {
  position: relative;
  display: grid;
  align-items: center;
  grid-template-columns: 1fr 0.5fr 1fr;
  margin: 0 auto;
  margin-right: 0;
  margin-left: 50px;
  justify-content: end;
}

.headerText {
  margin: 0 auto;
  text-align: start;
}

.brandName {
  font-size: 7rem;
  font-weight: 700;
}
.headerButtons {
  margin-left: 5px;
  padding: 20px 0;
}
.headerButtons button {
  background-color: #4fe1f9;
  border: 0;
  appearance: none;
  text-align: center;
  align-items: center;
  border-radius: 12px;
  padding: 12px 30px;
  box-shadow: 1px 2px 8px 0 rgba(0,0 ,0, 0.5);
  transition: all 0.3s ease;
}
.headerButtons button:hover {
  background-color: #24e2ff;
  border-radius: 20px;
  box-shadow: 1px 2px 15px 0 rgba(0,0 ,0, 0.5);
}
.headerButtons a {
  appearance: none;
  text-decoration: none;
  font-size: 1.1rem;
  color: white;
}
.logo {
  z-index: 1;
  position: absolute;
  top: 50%;
  left: 65%;
  transform: translate(-50%, -50%);
}

.logo_envoyage {
  width: 80%;
}

.brandImage {
  height: 100vh;
  position: absolute;
  top: 0;
  right: 0;
}

.gridBrandImage {
  position: relative;
}

.brandSlogan {
  margin-left: 5px;
  font-size: 2rem;
  font-weight: 700;
}
  .about {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px 0 150px 0;
    width: 90%;
    margin: 0 auto;
    gap: 70px;
  }
  .aboutSectionsContainer {
    display: none;
    flex-direction: column;
    gap: 400px;
  }
  .aboutSection {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .aboutSectionType1 {
    width: 70%;
  }
  .aboutSectionType2 {
    margin-left: 30%;
  }
  .containerSectionTop {
    height: 50vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .planeImage {
    position: absolute;
    top: 0;
    right: 0;
  }
  .containerSectionMiddle {
    height: 30vh;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
  }
  .containerSectionBottom {
    height: 70vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 50px;
  }
  .aboutSectionHexagonLeft {
    position: absolute;
    left: 0;
  }
  .aboutBorderHexaLeft {
  }
  .aboutSectionHexagonRight {
    position: absolute;
    right: 0;
  }
  .aboutBorderHexaRight {
    transform: scaleX(-1);
  }

  .arrow {
    position: absolute;
    align-items: center;
    margin: 0 auto;
    width: 100%;
    z-index: 2;
  }
  .arrowAboutSteps {
    top: -4%;
    left: 55%;
  }
  .arrowAboutSteps svg {
    transform: rotate(10deg);
  }

  .arrowTransitionSteps {
    left: 25%;
  }
  .arrowTransitionSteps svg {
    transform: rotate(-20deg) scale(-1, 1);
  }
  .arrowSVG {
    width: 150px;
  }
  .separationLine {
    width: 100%;
    height: 10px;
    background-color: #4fe1f9;
  }
  /* steps */

  .steps {
    position: relative;
    background-color: #efefef;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    gap: 70px;
    z-index: 1;
  }
  .steps .step01 {
    padding: 150px 0 100px 0;
  }
  .stepsPart1 {
    
  }
  .step {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 90%;
    gap: 200px;
  }
  .stepTop {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 90%;
  }
  .stepContent {
    display: flex;
    flex-direction: column;
    gap: 100px;
  }
  .stepTitle {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .stepTitle .text {
    margin-left: 50px;
    display: flex;
    gap: 5px;
  }
  .stepText {
    margin-left: 50px;
    width: 75%;
  }
  .stepNumber {
    position: absolute;
    font-size: 10rem;
    font-weight: 700;
    opacity: 30%;
  }
  .stepImage {
    width: 350px;
  }
  .stepAds {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-left: 50px;
  }
  .stepAds .stepText {
    margin-left: 0;
  }
  .stepAds .stepButton {
    border: 0;
    appearance: none;
    padding: 15px 100px;
  }
  .transition {
    width: 100%;
  }
  .scrollAds {
    width: 100vw;
    overflow-x: auto;
    display: flex;
    gap: 20px;
    margin-left: 0;
  }
  .containerAnnonces {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: scroll;
    gap: 20px;
    margin-left: 80px;
    scroll-behavior: smooth; /* Effet de défilement en douceur */
    user-select: none; /* Empêcher la sélection du texte lors du défilement */
    width: max-content; /* Ajuster la largeur du conteneur pour permettre le défilement infini */
    white-space: nowrap; /* Empêcher le saut à la ligne des cartes */
    padding-bottom: 20px; /* Ajouter un peu d'espace en bas pour éviter le saut abrupt */
    cursor: grab; /* Curseur de défilement au survol */
    cursor: -webkit-grab; /* Pour la compatibilité avec les navigateurs basés sur WebKit */
  }

  .card {
    border: none;
    border-radius: 20px;
    min-width: 500px; /* Ajuster la largeur de vos cartes */
    pointer-events: auto;
  }
  .containerAnnonces .active {
    cursor: grabbing;
  }
  .colorTopAnnonce {
    border-radius: 40px;
    height: 40px;
    width: 90%;
    margin: 0 auto;
  }
  .topCard {
    display: flex;
    flex-direction: row;
    padding: 0 50px 30px 50px;
    align-items: center;
    justify-content: space-between;
  }
  .card-footer {
    width: 100%;
    border-radius: 0 0 40px 40px;
    background-color: #d9d9d9;
  }

  .wrapper {
    width: 100%;
    position: relative;
  }
  .wrapper i {
    top: 50%;
    height: 50px;
    width: 50px;
    cursor: pointer;
    font-size: 1.25rem;
    position: absolute;
    text-align: center;
    line-height: 50px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.23);
    transform: translateY(-50%);
    transition: transform 0.1s linear;
  }
  .wrapper i:active {
    transform: translateY(-50%) scale(0.85);
  }
  .wrapper i:first-child {
    left: 23px;
    z-index: 20;
  }
  .wrapper i:last-child {
    right: 23px;
    z-index: 20;
  }
  .wrapper .carousel {
    display: grid;
    grid-auto-flow: column;
    /* grid-auto-columns: calc((100% / 4) - 12px); */
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 80px;
    border-radius: 8px;
    margin-left: -18%;
    scroll-behavior: smooth;
    scrollbar-width: none;
  }
  .carousel::-webkit-scrollbar {
    display: none;
  }
  .carousel.no-transition {
    scroll-behavior: auto;
  }
  .carousel.dragging {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }
  .carousel.dragging .card {
    cursor: grab;
    user-select: none;
  }
  .carousel :where(.card, .img) {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .carousel .card {
    scroll-snap-align: start;
    height: 342px;
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.29);
    list-style: none;
    background: #fff;
    cursor: pointer;
    flex-direction: column;
    border-radius: 40px;
  }


  /* Step 02 */
  .parentHexaSVGWhite {
    position: absolute;
    left: -15%;
    bottom: -40%;
    z-index: 6;
  }
  .HexaSVGWhite {
    width: 700px;
  }
  .step02 {
    padding: 100px 0 200px 0;
    align-items: flex-end;
    position: relative;
  }
  .step02Top {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 60%;
   
  }

  .arrowStep2Step3 {
    left: 50%;
    top: 100%;
    z-index: 5;
  }
  .arrowStep2Step3 svg {
  }
  /* Step 03 */

  .backgroundImageStep03 {
    position: absolute;
    z-index: -1;

  }
  .parentHexaSVGBlue {
    position: absolute;
    right: -15%;
    bottom: 40%;
  }
  .HexaSVGBlue {
    width: 600px;
  }

  .step03 {
    padding: 200px 0;
    position: relative;
  }
  .stepsPart2 {
    z-index: 2;
    background-color: transparent;
  }
  .step03 .stepNumber {
    color: white;
    position: absolute;
    font-size: 10rem;
    font-weight: 700;
    opacity: 30%;
  }
  .step03 .stepContent {
    
  }
  .step03 .stepText {
    width: 60%;
  }
.reverseHighlight {
    background-color: #1a849c;
  }
  
  /* Step 04 */ 
   
  .arrowStep3Step4 {
    top: 63%;
    left: 40%;
  }
  .arrowStep3Step4 svg {
    transform: rotate(-10deg) scale(-1,1);
  }
  .stepsPart3{
    padding: 200px 0;
  }
  .step04 {
    padding:  0;
  }
  .step04 .stepText {
   width: 60%;
  }
  .step04Top {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 30px;
  }
  .headerStep {
    margin: 0 auto;
  }

  /* faq */


  .faq {
    width: 100%;
    z-index: 1;
    display: flex;
    align-items: center;
    padding: 100px 0px 250px 100px;
  }
  .faqContent {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .faqText {
    font-size: 3rem;
  }
  .faqScroller {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .faqWrapper {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    gap: 20px;
    margin: 0 auto;
    width:90%;
    overflow-x: auto;
  }
  .faqWrapper * {
  user-select: none; /* Disable text selection */
  -webkit-user-select: none; /* Disable text selection for Safari */
  -moz-user-select: none; /* Disable text selection for Firefox */
  -ms-user-select: none; /* Disable text selection for Internet Explorer/Edge */
}
  .faqWrapper .col {
    padding: 40px 40px 80px 40px;
    background-image: url(../svg/effect_faq.svg);
    background-color: #3F3F40;
    border: 6px solid #4fe1f9;
    width: 110%;
    ;
  }
  .faqWrapper .cardNumber {
    font-size: 5rem;
  }
  .faqWrapper .carousel {
    display: grid;
    grid-auto-flow: column;
    /* grid-auto-columns: calc((100% / 4) - 12px); */
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 80px;
    border-radius: 8px;
    margin-left: 0%;
    scroll-behavior: smooth;
    scrollbar-width: none;
    justify-items: flex-start;
  }
  .faqWrapper .card {
    height: auto;
  }
  .faqWrapper .cardFaq {
    display: flex;
    flex-direction: column;
    gap: 40px;
  }
  .separationFooterStep04 {
    margin-top: -70px;
    height: 50px;
    width: 100%;
    background-color: #4fe1f9;
  }
  .colorTopAnnonce {
    border-radius: 40px;
    height: 40px;
    width: 100%;
    margin: 0 auto;
    border-radius: 30px;
    background-color: #4fe1f9;
  }
  .accordion {
  /* display: none; */
  width: 100%;
z-index: 2;
}

.accordion-item {
  border: 0;
  background: none;
  border-radius: 20px;
  margin-bottom: 10px;
}

.accordion-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  color: #767676;
  font-size: 1.6rem;
  cursor: pointer;
  transition: color 0.3s ease;
}

.accordion-header.active {
  color: #21A5C3; /* Change font color when active */
}

.accordion-content {
  margin-top: 15px;
  padding: 10px 20px;
  border-radius: 30px;
  font-size: 1.1rem;
  background-image: url('../svg/bg-acordeon.svg');
  border: 0;
  transition: max-height 0.3s ease, opacity 0.3s ease;
  max-height: 0;
  opacity: 0;
  overflow: hidden;
}

.accordion-content.active {
  max-height: 500px; /* Arbitrary value that can accommodate your content */
  opacity: 1;
}

.accordion-content p {
  margin: 0;
}

/* Media Query for smaller screens */
@media (max-width: 600px) {
  .aboutSectionsContainer {
    display: none;
  }

  .accordion {
    display: block;
  }
}
</style>
