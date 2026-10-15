---
title: "Scientist · Optics and Imaging"
layout: single
author_profile: true
classes: wide
excerpt: "Optical instrumentation, fluorescence lifetime imaging and open tools for microscopy at LOCI, University of Wisconsin–Madison."
feature_row:
  - image_path: /assets/images/teasers/research.svg
    alt: "Line drawing of a focused beam and its point spread function"
    title: "Research"
    excerpt: "Metabolic FLIM, custom optical instruments, automated microscopy and open FLIM software."
    url: /research/
    btn_label: "Research themes"
    btn_class: "btn--primary"
  - image_path: /assets/images/teasers/interactive.svg
    alt: "Line drawing of a slider controlling a decay curve"
    title: "Interactive"
    excerpt: "Explorable explanations of fluorescence lifetime imaging that run in your browser."
    url: /interactive/
    btn_label: "Try the widgets"
    btn_class: "btn--primary"
  - image_path: /assets/images/teasers/cv.svg
    alt: "Line drawing of a document"
    title: "Curriculum vitae"
    excerpt: "Appointments, publications, editorial roles and service, ready to print."
    url: /cv/
    btn_label: "Read the CV"
    btn_class: "btn--primary"
---

I specialize in optical instrumentation and data-driven biomedical imaging, including microscope development and autofluorescence techniques for assessing tissue metabolism. I work at the [Laboratory for Optical and Computational Instrumentation (LOCI)](https://loci.wisc.edu/) and [Cell Imaging](https://cellimaging.wisc.edu/), University of Wisconsin–Madison.
{: .home-lead}

{% include feature_row %}

## News

<ul class="news-list">
{% for item in site.data.news limit: 4 %}
  <li><time datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: "%b %Y" }}</time> <span>{{ item.text | markdownify | remove: '<p>' | remove: '</p>' | strip }}</span></li>
{% endfor %}
</ul>
