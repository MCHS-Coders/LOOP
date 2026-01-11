# Welcome to LAMPREY! (LOOP)
[![Documentation](https://img.shields.io/badge/wiki-docs-blue)](https://github.com/MCHS-Coders/LOOP/wiki)
[![Issues](https://img.shields.io/badge/issues-tracker-red)](https://github.com/MCHS-Coders/LOOP/issues)
[![Q&A](https://img.shields.io/badge/Q%26A-discussions-green)](https://github.com/MCHS-Coders/LAMPREY/discussions/3)

## The goal
**LAMPREY** is a project dedicated to **saving lives**, by allowing proactive efforts via **mesh networks**, deployed into **rural areas** to assist with **forecasting, prediction, mitigation, and studying meteorological events**.
This project consists of **hardware and software stacks**. This is the **hardware stack**.

## Radio communications
**LAMPREY** must have a way to communicate to any nearby devices, including over the mesh network. **Radio Communications** are crucial.
For this reason, we utilize many technologies to ensure reliability, ranging from **LoRA**, to **patch antennas** machined directly onto **PCBs**.
This repository will include the drivers, and firmware stack.

### LoRA-based communication
**LAMPREY** uses **LoRa** (**Lo**w power long-**Ra**nge) frequencies to communicate between devices in the **mesh network**.
These frequencies are **part of unregulated ISM bands**, and use **very little power**, and devices **may be configured for security**.

### Cellular, WiFI and Bluetooth-LE communication
To connect to **consumer devices**, the mesh network **must** utilize networks commonly used by mainstream devices, including **phones, and laptops**.
**WiFi-2.4GHz** and **Bluetooth-LE** (**BLE** for short,) support will likely be present in our prototype, **emergency cellular network** support will not be present in the prototype due to **legal and technical concerns**.

### Downlinking images from GOES-R series
In order to downlink images, the prototype will utilize **patch antennas**, etched/machined directly onto the **PCB**.
Downlinking images is completely **passive**, and **receive-only**. The specifics of the patch antenna have not been decided yet.
Ideally, a **single array** of these **patch antennas** on a *single device* should be able to downlink. This may be done with a variety of solutions.
One promising candidate is a **ceramic patch antenna**, or formally known as a **Dielectric Resonator Antenna**.

## Cross-Platform Application
The **Cross-Platform** application will be critical to implement. It will ideally be portable to windows, linux, ios, and android devices.
This application will include **safety awareness** videos, of which have been recorded by AISES teammates, and will be accessible directly from the application offline.
The application will **communicate with the mesh network**, through **Wi-Fi** and **Bluetooth-LE (BLE)**, and utilize the newfound data from these nodes to forecast.

## Safety and Testing
While testing is *non-existent* at this *early stage* of development, safety-focused designs have been **well-thought out**.
Development has even been delayed for the sake of safe deployment.
**Safety is always our first concern!** This project is dedicated to **saving lives**, after all!

## Checklist
- [ ] **Mesh Network Weather Probes**
  - [ ] Utilize **solar power** on mesh networks
  - [ ] Support **LoRa-based** mesh network communication
  - [ ] Support **Wi-Fi** communications
  - [ ] Support **Bluetooth-LE** communications
  - [ ] Successfully utilize **Patch Antennas** for **GOES-R**
  - [ ] Ensure **safety**, pass all **tests** and **checks**
  - [ ] Have a **<ins>functional prototype</ins>**

- [ ] **LOOP Software Stack**
  - [ ] Skeleton code implemented
  - [ ] **UI** and **UX** design
  - [ ] Correctly implement support for **hardware**
  - [ ] Add safety awareness videos to risk awareness library
  - [ ] Functional firmware implementation
  - [ ] Functional cross-platform application implementation
  - [ ] Have a **<ins>functional prototype</ins>**

**If any one of these is not ready by the presentation, please note very much effort has been poured into this project.**
**PLEASE let us know of your concerns for this project at [Q&A] if you see fit.**

## DEVELOPERS
**Ethan and Bryson Lee** are the only developers on this project.

[wiki]: https://github.com/MCHS-Coders/LOOP/wiki
[issues]: https://github.com/MCHS-Coders/LOOP/issues
[Q&A]: https://github.com/MCHS-Coders/LAMPREY/discussions/3
