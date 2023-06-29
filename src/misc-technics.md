# Midmesh

## Create Midmesh Automatically
1. Click Midmesh Ribbon > Automatic
2. Set **extraction size** (element size) and **defeature openings width**
3. Sometimes there would be defects for the midmesh. Manually repair as follow will be helpful.

<p align="center">
  <img src="../img/midmesh/midmesh-automatic.png" width="800">
  <img src="../img/midmesh/midmesh-result.png" width="800">
<p>

## Repair Omitted Region
1. Click Midmesh Ribbon > Create Midedge. Select nodes and guide to create a midmesh boundary.
2. Click Midmesh Ribbon > Repair/Fill. Select the enclosed boundary to fill the region with mesh.

<p align="center">
  <img src="../img/midmesh/create-midedge.png" width="800">
  <img src="../img/midmesh/fill-face.png" width="800">
  <img src="../img/midmesh/fill-completed.png" width="800">
<p>

## Repair Overfilled Region
1. Click Midmesh Ribbon > Edit Topology. Select line geometry to imprint the midmesh.
2. Click the left button to switch different mode
3. After imprint, Delete the elements within the hole manually

<p align="center">
  <img src="../img/midmesh/imprint-a.png" width="800">
  <img src="../img/midmesh/imprint-b.png" width="800">
  <img src="../img/midmesh/imprint-a-result.png" width="800">
  <img src="../img/midmesh/imprint-b-result.png" width="800">
<p>
