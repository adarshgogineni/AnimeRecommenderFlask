document.addEventListener('DOMContentLoaded', function () {
    particlesJS('particles-js', {
        particles: {
            number: {
                value: 250, // The number of particles
                density: {
                    enable: true,
                    value_area: 800 // The area (in px^2) used to calculate the number of particles
                }
            },
            color: {
                value: '#000000' // The color of the particles (can be an array of colors or a single color)
            },
            shape: {
                type: 'circle', // Shape of the particles (e.g., 'circle', 'edge', 'triangle', 'polygon', 'star', 'image')
                stroke: {
                    width: 0,
                    color: '#000000'
                },
                polygon: {
                    nb_sides: 5 // Number of sides of the polygon (if shape type is 'polygon')
                }
            },
            opacity: {
                value: 0.5,
                random: false,
                anim: {
                    enable: false,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 3,
                random: true,
                anim: {
                    enable: false,
                    speed: 40,
                    size_min: 0.1,
                    sync: false
                }
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#ffffff',
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 6,
                direction: 'none', // Can be 'none', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'left', 'top-left'
                random: false,
                straight: false,
                out_mode: 'out', // What happens to particles at the edge of the canvas ('out', 'bounce')
                bounce: false,
                attract: {
                    enable: false,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: {
                    enable: true,
                    mode: 'repulse' // Other modes: 'grab', 'bubble', 'repulse'
                },
                onclick: {
                    enable: true,
                    mode: 'push' // Other modes: 'push', 'remove', 'bubble', 'repulse'
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 1
                    }
                },
                bubble: {
                    distance: 400,
                    size: 40,
                    duration: 2,
                    opacity: 8,
                    speed: 3
                },
                repulse: {
                    distance: 200,
                    duration: 0.4
                },
                push: {
                    particles_nb: 4
                },
                remove: {
                    particles_nb: 2
                }
            }
        },
        retina_detect: true // Enables retina display support
    });
});
