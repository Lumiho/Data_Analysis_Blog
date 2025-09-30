import React from 'react';

interface InteractiveVisualizationProps {
  src: string;
  width?: string;
  height?: string;
}

export default function InteractiveVisualization({ 
  src, 
  width = "100%", 
  height = "600px" 
}: InteractiveVisualizationProps) {
  return (
    <div className="my-8">
      <iframe
        src={src}
        width={width}
        height={height}
        style={{ border: 'none', borderRadius: '8px' }}
        title="Interactive Visualization"
      />
    </div>
  );
} 