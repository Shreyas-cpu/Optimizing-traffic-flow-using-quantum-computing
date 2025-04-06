# Realistic Traffic Sample Videos for QuantumPlators

This directory contains realistic traffic simulation videos for testing the QuantumPlators Traffic Management System. The videos feature detailed animations and realistic traffic scenarios.

## Video Descriptions

1. `pedestrian_sample.webm`
   - 10-second HD video (640x480) showing realistic pedestrian movement
   - Features:
     * Animated walking cycles with arm and leg movements
     * Pedestrians using crosswalk
     * Random waiting behavior at crossings
     * Multiple pedestrians moving in both directions
     * Realistic sidewalk and road layout

2. `two_wheeler_sample.webm`
   - 10-second HD video showing two-wheeler traffic
   - Features:
     * Detailed motorcycle/scooter representations
     * Realistic vehicle movement with bounce effects
     * Animated riders
     * Two-way traffic flow
     * Multiple vehicles with different speeds

3. `car_sample.webm`
   - 10-second HD video showing car traffic
   - Features:
     * Detailed car models with different colors
     * Realistic suspension effects (vehicle bounce)
     * Rotating wheels with spokes
     * Vehicle shadows
     * Multiple cars in different lanes

## Environment Details

- Road Layout:
  * Two-lane road with proper markings
  * Dedicated crosswalk with zebra stripes
  * Sidewalks on both sides
  * Green areas with decorative elements

- Visual Effects:
  * Sky-blue background
  * Green landscaping
  * Realistic shadows
  * Smooth animations
  * Timestamp overlay

## How to Generate New Videos

1. Open `generate_videos.html` in a web browser
2. Each traffic type (pedestrians, two-wheelers, cars) has its own preview window
3. Click the respective "Download" button to generate a 10-second video
4. Videos are saved in WebM format with VP9 codec

## Using the Videos

1. In the QuantumPlators interface:
   - Upload `pedestrian_sample.webm` for pedestrian detection
   - Upload `two_wheeler_sample.webm` for two-wheeler detection
   - Upload `car_sample.webm` for car detection

2. The videos provide consistent test data with:
   - Clear object visibility
   - Various traffic densities
   - Different movement patterns
   - Realistic traffic flow scenarios

These sample videos offer a controlled yet realistic environment for testing and demonstrating the QuantumPlators traffic management system's detection and optimization capabilities.

## Technical Specifications

- Resolution: 640x480 pixels
- Frame Rate: 30 FPS
- Duration: 10 seconds
- Format: WebM (VP9 codec)
- Features:
  * Timestamp overlay
  * Smooth animations
  * Physics-based movement
  * Realistic traffic patterns
