---
title: "Automated and agentic microscopy"
excerpt: "Control software that connects acquisition to analysis: AI-assisted whole slide imaging, annotation-driven targeted acquisition from QuPath, and LLM agents steering the microscope over MCP."
order: 3
header:
  teaser: /assets/images/teasers/agentic.svg
---

Microscopes are increasingly run by software that decides what to image next. I work on control software that connects acquisition to analysis, so the analysis can decide where, how and with which modality to image next. The three projects below build on each other: SmartPath automated whole slide imaging, QPSC lets a pathologist's annotations drive acquisition, and DReAMS hands the steering to an AI agent.

## SmartPath: automatic multimodal whole slide imaging

[SmartPath](https://github.com/uw-loci/smart-wsi-scanner) is an open-source whole slide histopathology imaging system. It switches modality automatically, finds regions of interest with deep learning, and processes images as they are acquired. Acquisition runs from Jupyter notebooks, with [Pycro-Manager](https://pycro-manager.readthedocs.io/) controlling the hardware through Micro-Manager, OpenScan for laser scanning, and QuPath and Fiji for viewing and analysis.

- [Hardware-software co-design of an open-source automatic multimodal whole slide histopathology imaging system](https://doi.org/10.1117/1.JBO.28.2.026501). Li B, Nelson MS, Chacko JV, Cudworth N, Eliceiri KW. *J. Biomed. Opt.* 28(2), 026501 (2023).

## QPSC: QuPath Scope Control

[QPSC](https://github.com/uw-loci/QPSC) brings microscope control into [QuPath](https://qupath.github.io/). You draw annotations on an overview image or a slide-scanner image, QPSC maps them to stage coordinates, acquires high-resolution tiles at those locations, and stitches them into pyramidal OME-ZARR images that come back into the same QuPath project. Each acquisition can seed the next one at higher resolution or in a different modality.

- **Modalities:** brightfield, multi-channel widefield immunofluorescence, combined brightfield and fluorescence, polarized light microscopy (PPM), and laser scanning (two-photon, SHG, confocal; in beta).
- **Architecture:** Java QuPath extensions for the interface, workflows and coordinate transforms; a Python command server for acquisition, hardware control and image processing; Micro-Manager underneath through Pycro-Manager.
- **Code:** [uw-loci/QPSC](https://github.com/uw-loci/QPSC) is the entry point, with installation guides and links to the component repositories.

## DReAMS: Data-Reactive Acquisition and Microscope Steering

[DReAMS](https://github.com/uw-loci/dreams) exposes a real microscope to an LLM agent through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), so the agent can observe, decide and steer the acquisition itself. It ships three MCP servers:

- **Microscope:** snap images, move the stage, read its position and run tile scans, through Micro-Manager and Pycro-Manager.
- **Datasets:** archive captures to the lab file server and fetch them back.
- **QuPath:** open images, list annotations, detect cells and export regions from a running QuPath.

Images are passed as file paths, so image data never travels through the agent's context. Any MCP client can connect; a GitHub Copilot CLI configuration is included. The same skeleton has been pruned down to drive a telescope, as a check that the design is not tied to one instrument.

- Poster at Focus on Microscopy 2026, Stockholm.
