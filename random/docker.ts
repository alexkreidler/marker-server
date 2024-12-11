import fs from 'fs/promises';
import path from 'path';

// Interface to represent a layer in the OCI manifest
interface OCILayer {
  mediaType: string;
  digest: string;
  size: number;
  annotations?: Record<string, string>;
}

// Function to convert bytes to human-readable format
function formatBytes(bytes: number): string {
  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  let size = bytes;
  let unitIndex = 0;

  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024;
    unitIndex++;
  }

  return `${size.toFixed(2)} ${units[unitIndex]}`;
}

async function analyzeLayers(filePath: string) {
  try {
    // Read the file
    const fileContent = await fs.readFile(filePath, 'utf8');
    const manifests = JSON.parse(fileContent);

    // Iterate through each manifest
    manifests.forEach((manifest: any, index: number) => {
      console.log(`Manifest ${index + 1}:`);
      console.log(`Reference: ${manifest.Ref}`);
      
      const layers: OCILayer[] = manifest.OCIManifest.layers;
      let totalSize = 0;

      console.log('\nLayers:');
      layers.forEach((layer, layerIndex) => {
        console.log(`  Layer ${layerIndex + 1}:`);
        console.log(`    Media Type: ${layer.mediaType}`);
        console.log(`    Digest: ${layer.digest}`);
        console.log(`    Size: ${formatBytes(layer.size)}`);
        
        if (layer.annotations) {
          console.log('    Annotations:');
          Object.entries(layer.annotations).forEach(([key, value]) => {
            console.log(`      ${key}: ${value}`);
          });
        }
        
        totalSize += layer.size;
      });

      console.log(`\nTotal Layers: ${layers.length}`);
      console.log(`Total Size: ${formatBytes(totalSize)}\n`);
    });
  } catch (error) {
    console.error('Error reading or parsing the file:', error);
  }
}

// Usage
const manifestPath = "./manifest.json"
analyzeLayers(manifestPath);

export {};