<!-- ABOUT THE PROJECT -->

## About The Project

This project, "Volume Controller", uses a custom made module called HandTrackingModule that utlizes OpenCV and MediaPipe to track and detect hands and places landmarks. By using NumPy, OpenCV, and pycaw (Python Core Audio Windows Library), we are able to change the volume of the device based on the distance between the thumb landmark and the index finger landmark.

Made by: [Nathan Xie](https://github.com/na3th9n)

### Built With

- Python
- OpenCV
- MediaPipe
- NumPy
- [pycaw](https://github.com/AndreMiras/pycaw)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

All libraries are located in requirements.txt.

- pip
  ```sh
  pip install -r requirements
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/na3th9n/HandTrackingApp.git
   ```
2. Install libraries
   ```sh
   pip install -r requirements.txt
   ```
3. Run VolumeControl.py

## Usage

N/A

## Contact

Linkedin: [Linkedin](https://www.linkedin.com/in/nathanxie/)

Email: na3than.xie@gmail.com

Project Link: [N/A]()

## Acknowledgments

N/A

## Additional Notes

Hand Tracking:

- when the mp packing is tracking hands, it creates landmarks across the hands (dots) to detect the motion and where the image is
- all the landmarks have unique ids and also position on the screen

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
