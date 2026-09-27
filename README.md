# soldering-projects

A curated, moderated list of acclaimed open-source projects you can build on ESP32 modules.

Every entry is open source, runs on the ESP32 family as a primary target, is well regarded
(500+ GitHub stars or notable coverage), and is still maintained. The list is audited
weekly against those rules, so dead or relicensed projects get flagged. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the full criteria and how to suggest a project.

🔧 = open hardware (schematics/PCB published) · ⚠️ = moderator note

<!-- BEGIN LIST -->
### Home automation & smart home

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [ESPEasy](https://github.com/letscontrolit/ESPEasy) | Plugin-based sensor and actuator firmware configured entirely from a web interface | ![stars](https://img.shields.io/github/stars/letscontrolit/ESPEasy?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/letscontrolit/ESPEasy?style=flat-square&label=) |
| [ESPHome](https://github.com/esphome/esphome) | YAML-configured firmware for ESP32 devices with native Home Assistant integration | ![stars](https://img.shields.io/github/stars/esphome/esphome?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/esphome/esphome?style=flat-square&label=) |
| [ESPresense](https://github.com/ESPresense/ESPresense) | Room-level presence detection from BLE advertisements using a node per room | ![stars](https://img.shields.io/github/stars/ESPresense/ESPresense?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/ESPresense/ESPresense?style=flat-square&label=) |
| [openHASP](https://github.com/HASwitchPlate/openHASP) | Turns ESP32 touchscreens into customizable Home Assistant control panels over MQTT | ![stars](https://img.shields.io/github/stars/HASwitchPlate/openHASP?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/HASwitchPlate/openHASP?style=flat-square&label=) |
| [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) | Bridges BLE, 433 MHz, IR and LoRa devices to MQTT | ![stars](https://img.shields.io/github/stars/1technophile/OpenMQTTGateway?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/1technophile/OpenMQTTGateway?style=flat-square&label=) |
| [ratgdo (ESPHome)](https://github.com/ratgdo/esphome-ratgdo) | Local control of Chamberlain/LiftMaster Security+ garage door openers | ![stars](https://img.shields.io/github/stars/ratgdo/esphome-ratgdo?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/ratgdo/esphome-ratgdo?style=flat-square&label=) |
| [Tasmota](https://github.com/arendst/Tasmota) | Alternative firmware for ESP-based smart devices with web UI, MQTT, rules and OTA updates | ![stars](https://img.shields.io/github/stars/arendst/Tasmota?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/arendst/Tasmota?style=flat-square&label=) |

### LED & lighting

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [WLED](https://github.com/wled/WLED) | Addressable LED strip controller with 100+ effects, web/app control and sound reactivity | ![stars](https://img.shields.io/github/stars/wled/WLED?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/wled/WLED?style=flat-square&label=) |

### Energy, climate & sensing

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [EMS-ESP32](https://github.com/emsesp/EMS-ESP32) | Reads and controls Bosch/Buderus/Nefit boilers and heat pumps over the EMS bus | ![stars](https://img.shields.io/github/stars/emsesp/EMS-ESP32?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/emsesp/EMS-ESP32?style=flat-square&label=) |
| [OpenDTU](https://github.com/tbnobody/OpenDTU) | Local monitoring and power limiting for Hoymiles solar micro-inverters | ![stars](https://img.shields.io/github/stars/tbnobody/OpenDTU?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/tbnobody/OpenDTU?style=flat-square&label=) |

### Radio, mesh & networking

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [ESP32-Paxcounter](https://github.com/cyberman54/ESP32-Paxcounter) | Counts nearby WiFi and BLE devices to estimate crowd density, reports via LoRaWAN | ![stars](https://img.shields.io/github/stars/cyberman54/ESP32-Paxcounter?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/cyberman54/ESP32-Paxcounter?style=flat-square&label=) |
| [Meshtastic](https://github.com/meshtastic/firmware) | Off-grid encrypted LoRa mesh messaging for ESP32 and other boards | ![stars](https://img.shields.io/github/stars/meshtastic/firmware?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/meshtastic/firmware?style=flat-square&label=) |

### Security research tools

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [Bruce](https://github.com/BruceDevices/firmware) | Multi-tool firmware for red-team research on M5Stack, Cardputer and similar boards ⚠️ _Only use on networks and devices you own or are authorized to test_ | ![stars](https://img.shields.io/github/stars/BruceDevices/firmware?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/BruceDevices/firmware?style=flat-square&label=) |
| [ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder) | WiFi and Bluetooth offensive/defensive research suite with touchscreen UI ⚠️ _Only use on networks and devices you own or are authorized to test_ | ![stars](https://img.shields.io/github/stars/justcallmekoko/ESP32Marauder?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/justcallmekoko/ESP32Marauder?style=flat-square&label=) |

### Audio & voice

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [ESP-BOX](https://github.com/espressif/esp-box) | Espressif's open AIoT voice dev kit with speech recognition demos 🔧 | ![stars](https://img.shields.io/github/stars/espressif/esp-box?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/espressif/esp-box?style=flat-square&label=) |
| [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | LLM-powered voice assistant firmware supporting dozens of ESP32-S3 boards | ![stars](https://img.shields.io/github/stars/78/xiaozhi-esp32?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/78/xiaozhi-esp32?style=flat-square&label=) |
| [yoRadio](https://github.com/e2002/yoradio) | Web radio player with display, rotary encoder and IR remote support | ![stars](https://img.shields.io/github/stars/e2002/yoradio?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/e2002/yoradio?style=flat-square&label=) |

### Displays, clocks & gadgets

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [EPDiy](https://github.com/vroland/epdiy) | Driver board and library for parallel e-paper displays (Kindle panels etc.) 🔧 | ![stars](https://img.shields.io/github/stars/vroland/epdiy?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/vroland/epdiy?style=flat-square&label=) |
| [NerdMiner v2](https://github.com/BitMaker-hub/NerdMiner_v2) | Toy "lottery" Bitcoin solo miner with a stats display on cheap ESP32 boards | ![stars](https://img.shields.io/github/stars/BitMaker-hub/NerdMiner_v2?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/BitMaker-hub/NerdMiner_v2?style=flat-square&label=) |
| [Split-flap display](https://github.com/scottbez1/splitflap) | DIY split-flap display with ESP32 controller, laser-cut or 3D-printed 🔧 | ![stars](https://img.shields.io/github/stars/scottbez1/splitflap?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/scottbez1/splitflap?style=flat-square&label=) |
| [Watchy](https://github.com/sqfmi/Watchy) | Open-source ESP32 e-paper smartwatch 🔧 | ![stars](https://img.shields.io/github/stars/sqfmi/Watchy?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/sqfmi/Watchy?style=flat-square&label=) |

### Gaming & input

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [Bluepad32](https://github.com/ricardoquesada/bluepad32) | Bluetooth gamepad host for ESP32 supporting Xbox, PlayStation, Switch controllers | ![stars](https://img.shields.io/github/stars/ricardoquesada/bluepad32?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/ricardoquesada/bluepad32?style=flat-square&label=) |
| [Retro-Go](https://github.com/ducalex/retro-go) | Retro console emulator launcher (NES, GB, SMS, PCE, ...) for ESP32 handhelds | ![stars](https://img.shields.io/github/stars/ducalex/retro-go?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/ducalex/retro-go?style=flat-square&label=) |

### Robotics & CNC

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [ESP-Drone](https://github.com/espressif/esp-drone) | Mini quadcopter built around ESP32-S2/S3, controlled from a phone 🔧 | ![stars](https://img.shields.io/github/stars/espressif/esp-drone?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/espressif/esp-drone?style=flat-square&label=) |
| [FluidNC](https://github.com/bdring/FluidNC) | CNC motion controller firmware (successor to Grbl_ESP32) for mills, lasers and plotters | ![stars](https://img.shields.io/github/stars/bdring/FluidNC?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/bdring/FluidNC?style=flat-square&label=) |

### Frameworks & libraries

| Project | Description | Stars | Last commit |
|---|---|---|---|
| [Arduino core for ESP32](https://github.com/espressif/arduino-esp32) | Arduino core for the ESP32 family | ![stars](https://img.shields.io/github/stars/espressif/arduino-esp32?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/espressif/arduino-esp32?style=flat-square&label=) |
| [ESP-IDF](https://github.com/espressif/esp-idf) | Espressif's official IoT development framework | ![stars](https://img.shields.io/github/stars/espressif/esp-idf?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/espressif/esp-idf?style=flat-square&label=) |
| [ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP) | Bluetooth A2DP audio sink/source library | ![stars](https://img.shields.io/github/stars/pschatzmann/ESP32-A2DP?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/pschatzmann/ESP32-A2DP?style=flat-square&label=) |
| [esp32-camera](https://github.com/espressif/esp32-camera) | Camera driver for OV2640/OV3660/OV5640 and friends (ESP32-CAM) | ![stars](https://img.shields.io/github/stars/espressif/esp32-camera?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/espressif/esp32-camera?style=flat-square&label=) |
| [ESP32-HUB75-MatrixPanel-DMA](https://github.com/mrcodetastic/ESP32-HUB75-MatrixPanel-DMA) | DMA driver for HUB75 RGB LED matrix panels | ![stars](https://img.shields.io/github/stars/mrcodetastic/ESP32-HUB75-MatrixPanel-DMA?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/mrcodetastic/ESP32-HUB75-MatrixPanel-DMA?style=flat-square&label=) |
| [ESPAsyncWebServer](https://github.com/ESP32Async/ESPAsyncWebServer) | Asynchronous HTTP and WebSocket server | ![stars](https://img.shields.io/github/stars/ESP32Async/ESPAsyncWebServer?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/ESP32Async/ESPAsyncWebServer?style=flat-square&label=) |
| [IRremoteESP8266](https://github.com/crankyoldgit/IRremoteESP8266) | Send and receive infrared remote protocols (works on ESP32 too) | ![stars](https://img.shields.io/github/stars/crankyoldgit/IRremoteESP8266?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/crankyoldgit/IRremoteESP8266?style=flat-square&label=) |
| [LovyanGFX](https://github.com/lovyan03/LovyanGFX) | High-performance graphics library for SPI/I2C/parallel displays | ![stars](https://img.shields.io/github/stars/lovyan03/LovyanGFX?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/lovyan03/LovyanGFX?style=flat-square&label=) |
| [NimBLE-Arduino](https://github.com/h2zero/NimBLE-Arduino) | Lightweight BLE stack for Arduino, a drop-in replacement for the default one | ![stars](https://img.shields.io/github/stars/h2zero/NimBLE-Arduino?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/h2zero/NimBLE-Arduino?style=flat-square&label=) |
| [TFT_eSPI](https://github.com/Bodmer/TFT_eSPI) | Fast graphics library for SPI TFT displays | ![stars](https://img.shields.io/github/stars/Bodmer/TFT_eSPI?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/Bodmer/TFT_eSPI?style=flat-square&label=) |
| [WiFiManager](https://github.com/tzapu/WiFiManager) | Captive-portal WiFi configuration for ESP boards | ![stars](https://img.shields.io/github/stars/tzapu/WiFiManager?style=flat-square&label=) | ![last commit](https://img.shields.io/github/last-commit/tzapu/WiFiManager?style=flat-square&label=) |
<!-- END LIST -->

## How this list is maintained

- `projects.yml` is the source of truth. The tables above are generated from it, so don't edit them by hand.
- `python scripts/curate.py render` regenerates this README.
- `python scripts/curate.py audit` checks every entry against GitHub (stars, license, archived, last push). CI runs it on pull requests and every week.
