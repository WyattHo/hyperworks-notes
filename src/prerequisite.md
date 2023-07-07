# Prerequisite

## Terminologies about Product Data

### Product Lifecycle Management (PLM)
- The process of managing the entire lifecycle of a product, including:
  1. Conceive (specification, concept design)
  2. Design (detailed design, validation and analysis)
  3. Realise (manufacture, quality control)
  4. Service (sell, maintain, support, dispose)
- The core of PLM is 
  1. The creation and central management of all **product data** and 
  2. The technology used to access the information and knowledge
- `*.plmxml` represents the Siemens Product Lifecycle Management (PLM) XML file format

---

### Product Data Management (PDM)
- A business function within product lifecycle management (PLM)
- PDM serves as a **central knowledge repository**. The information being stored and managed will include engineering data such as
  1. Computer-aided design (CAD) models
  2. Drawings
  3. Associated documents
  4. **Metadata** (such as the owner of a file and the release status of the components)
- PDM will 
  1. control check-in and check-out of the product data to multi-user
  2. carry out engineering change management and release control
  3. build and manipulate the product structure **bill of materials (BOM)** for assemblies

---

### Metadata
- Metadata means data about data. Some examples include
  1. Time and date of creation
  2. Creator or author of the data
  3. File size
  4. ...

---

### Bill of Materials (BOM)
- BOM is a list of the raw materials, sub-assemblies, intermediate assemblies, sub-components, parts, and the quantities of each needed to manufacture an end product

<p align="center">
  <img src="../img/prerequisite/bom.png" width="600">
<p>

---

### References:
  - <https://en.wikipedia.org/wiki/Product_lifecycle>
  - <https://www.filetypeadvisor.com/extension/plmxml>
  - <https://en.wikipedia.org/wiki/Product_data_management>
  - <https://en.wikipedia.org/wiki/Metadata>
  - <https://en.wikipedia.org/wiki/Bill_of_materials>

---

## Model Hierarchy

### CAD Hierarchy
- Feature
  - The operations that are used to build **parts**, such as 
    - Extrude
    - Revolve
    - Sweep
    - ...
- Part
  - A single closed solid body created by features
- Instance 
  - A part, sketch, surface, or subassembly used in an Assembly
- Group
  - A collection of related parts in an assembly that move as one. A tool used to create a group
- Subassembly
  - An assembly used within another assembly
- Assembly
  - A collection of instances of parts, sketches, surfaces, or subassemblies
  - An environment where you can define both **position** and **movement** of a complete product or system

---

### CAE Hierarchy
- Components
  - Components collect and organize points, lines, surfaces, solids, elements and connectors
  - A component can be assigned **a property or material**, that assignment is applied to all elements within that component
  - **Indirect** property and material assignment is performed on the component level
  - **Direct** property and material assignment is performed directly on the elements themselves
- Parts
  - A part is an engineering representation of a physical part
  - A part can only contain components
- Part Instances
  - Part Instances are recognized from **PDM**, are automatically converted on import into HyperMesh
- Part Assemblies
  - A part assembly is a group of part assemblies and/or parts
- Model
  - The model is the root of the hierarchy
  - It represents the contents of the HyperMesh binary file and can contain part assemblies, parts, and components.

---

### References:
  - <https://superdope.onshape.com/help/Content/Glossary/glossary.htm?tocpath=_____22>
  - <https://help.altair.com/hwdesktop/hwx/topics/pre_processing/entities/components_r.htm>
  - <https://help.altair.com/hwdesktop/hwx/topics/pre_processing/model_build_and_assembly/part_assemblies_and_parts_organize_t.htm>
  - <https://help.altair.com/hwdesktop/hwx/topics/pre_processing/model_build_and_assembly/part_and_part_assembly_about_c.htm>
