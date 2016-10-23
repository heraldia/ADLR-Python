/*
 * Com S 336 HW 5 Three JS Scene Alex White
 * 
 * This scene is a kind of recreation of the outdated graphics from the old Super Nintendo game Star Fox
 * 
 * Includes at least 8 objects, some of which are hierarchically related.
 * Uses at least three types of geometry (cubes, spheres, planes, extrusions, etc.)
 * 	at least one of which is a model loaded from an OBJ file.
 * Has multiple lights
 * Has a skybox
 * Uses texture mapping on something other than the skybox
 * Has controls for the camera
 * Has at least one feature that is animated
 *  alexw-AlexWhite_ComS336HW5
 */

// a couple of example cube maps
//var path = "../images/park/";
//var path = "../images/sky/";
var path = "Textures/";
var imageNames = [
                  path + "px2.png",
                  path + "nx2.png",
                  path + "py2.png",
                  path + "ny2.png",
                  path + "pz2.png",        
                  path + "nz2.png"
                  ];


var axis = 'z';
var paused = false;
var camera;

//translate keypress events to strings
//from http://javascript.info/tutorial/keyboard-events
function getChar(event) {
if (event.which == null) {
 return String.fromCharCode(event.keyCode) // IE
} else if (event.which!=0 && event.charCode!=0) {
 return String.fromCharCode(event.which)   // the rest
} else {
 return null // special key
}
}

function cameraControl(c, ch)
{
  var distance = c.position.length();
  var q, q2;
  
  switch (ch)
  {
  // camera controls
  case 'w':
    c.translateZ(-0.5);
    return true;
  case 'a':
    c.translateX(-0.5);
    return true;
  case 's':
    c.translateZ(0.5);
    return true;
  case 'd':
    c.translateX(0.5);
    return true;
  case 'r':
    c.translateY(0.5);
    return true;
  case 'f':
    c.translateY(-0.5);
    return true;
  case 'j':
    // need to do extrinsic rotation about world y axis, so multiply camera's quaternion
    // on left
    q = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 1, 0),  5 * Math.PI / 180);
    q2 = new THREE.Quaternion().copy(c.quaternion);
    c.quaternion.copy(q).multiply(q2);
    return true;
  case 'l':
    q = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 1, 0),  -5 * Math.PI / 180);
    q2 = new THREE.Quaternion().copy(c.quaternion);
    c.quaternion.copy(q).multiply(q2);
    return true;
  case 'i':
    // intrinsic rotation about camera's x-axis
    c.rotateX(5 * Math.PI / 180);
    return true;
  case 'k':
    c.rotateX(-5 * Math.PI / 180);
    return true;
  case 'O':
    c.lookAt(new THREE.Vector3(0, 0, 0));
    return true;
  case 'S':
    c.fov = Math.min(80, c.fov + 5);
    c.updateProjectionMatrix();
    return true;
  case 'W':
    c.fov = Math.max(5, c.fov  - 5);
    c.updateProjectionMatrix();
    return true;

    // alternates for arrow keys
  case 'J':
    //this.orbitLeft(5, distance)
    c.translateZ(-distance);
    q = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 1, 0),  5 * Math.PI / 180);
    q2 = new THREE.Quaternion().copy(c.quaternion);
    c.quaternion.copy(q).multiply(q2);
    c.translateZ(distance)
    return true;
  case 'L':
    //this.orbitRight(5, distance)  
    c.translateZ(-distance);
    q = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 1, 0),  -5 * Math.PI / 180);
    q2 = new THREE.Quaternion().copy(c.quaternion);
    c.quaternion.copy(q).multiply(q2);
    c.translateZ(distance)
    return true;
  case 'I':
    //this.orbitUp(5, distance)      
    c.translateZ(-distance);
    c.rotateX(-5 * Math.PI / 180);
    c.translateZ(distance)
    return true;
  case 'K':
    //this.orbitDown(5, distance)  
    c.translateZ(-distance);
    c.rotateX(5 * Math.PI / 180);
    c.translateZ(distance)
    return true;
  }
  return false;
}

function handleKeyPress(event)
{
  var ch = getChar(event);
  if (cameraControl(camera, ch)) return;
  
  switch(ch)
  {
  case ' ':
    paused = !paused;
    break;
  case 'x':
    axis = 'x';
    break;
  case 'y':
    axis = 'y';
    break;
  case 'z':
    axis = 'z';
    break;
  default:
    return;
  }
}

function start()
{
  window.onkeypress = handleKeyPress;

  var scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera( 30, 1.5, 0.1, 1000 );
  camera.position.x = 0;
  camera.position.y = -95;
  camera.position.z = 0;
  camera.lookAt(new THREE.Vector3(0, -96, 20));
  
  var ourCanvas = document.getElementById('theCanvas');
  var renderer = new THREE.WebGLRenderer({canvas: ourCanvas});

  // Loads the six images
  // Note optional second parameter, this allows the texture to be used for refraction 
  // (and the texture still works for the skybox).
  var ourCubeMap = THREE.ImageUtils.loadTextureCube(imageNames);
  //var ourCubeMap = THREE.ImageUtils.loadTextureCube(imageNames, THREE.CubeRefractionMapping);
  
  // Use a built-in Three.js shader for cube maps
  var cubeMapShader = THREE.ShaderLib["cube"];
  cubeMapShader.uniforms[ "tCube" ].value = ourCubeMap;
  var material = new THREE.ShaderMaterial( {
      fragmentShader: cubeMapShader.fragmentShader,
      vertexShader: cubeMapShader.vertexShader,
      uniforms: cubeMapShader.uniforms,
      side: THREE.BackSide  // we'll only see the inside of the cube
  } );

  // Make a big ole cube for the skybox
  var geometry = new THREE.BoxGeometry( 1000, 1000, 1000 );

  // Create a mesh for the skybox using the cube shader as the material
  var cube = new THREE.Mesh( geometry, material );
  
  // Add it to the scene
  scene.add( cube );
  
  //Add spot light
  var spLight = new THREE.SpotLight(0xffffff, 1.75, 2000, Math.PI / 3);
  spLight.position.set(-100, 300, -50);
  scene.add(spLight);
  
  var ptLight = new THREE.PointLight(0xffffff, 1, 1000);
  ptLight.position.set(-6, -94, 50);
  scene.add(ptLight);
  
  var ptLight2 = new THREE.PointLight(0xE8890C, 6, 5);
  ptLight2.position.set(0, -97, 19.5);
  scene.add(ptLight2);
  
  var ptLight3 = new THREE.PointLight(0xffffff, 5, 6);
  ptLight3.position.set(-6, -93, 37);
  scene.add(ptLight3);
  
  var ptLight4 = new THREE.PointLight(0xffffff, 5, 6);
  ptLight4.position.set(-6, -94, 71);
  scene.add(ptLight4);
  
  //Add simple ground
  var groundTexture = THREE.ImageUtils.loadTexture("Textures/gradientground.png");
 
  var material = new THREE.MeshLambertMaterial({map:groundTexture});
  var ground = new THREE.Mesh(new THREE.PlaneGeometry(200, 200, 10, 10), material);
  ground.receiveShadow = true;
  ground.material.side = THREE.DoubleSide;
  ground.position.set(0, -100, 0);
  ground.rotation.x = -Math.PI / 2;
  scene.add(ground);

  
  var loader = new THREE.OBJLoader();
  //Don't mess up that arwing!
  loader.load('models/iPhone_6.obj', function(object, materials) {
  
  var material2 = new THREE.MeshLambertMaterial({color: 0x999999});
  
  object.traverse(function(child) {
	  if (child instanceof THREE.Mesh) {
		  
		  child.material = material2;
		  
		  child.castShadow = true;
		  child.receiveShadow = true;
	  }
  });  
  object.position.x = 0;
  object.position.y = 5;
  object.position.z = 0;
  object.scale.set(1,1,1);
  scene.add(object);
  });
  
  
  function render() {
    requestAnimationFrame( render );
    renderer.render(scene, camera);
  }

  render();
}

