import React from 'react';
import Image from 'next/image';

interface StaticGraphProps {
  src: string;
  alt: string;
  width: number;
  height: number;
}

interface InteractiveGraphProps {
  src: string;
  width?: string;
  height?: string;
}

export const StaticGraph: React.FC<StaticGraphProps> = ({ src, alt, width, height }) => {
  return (
    <div className="relative">
      <Image
        src={src}
        alt={alt}
        width={width}
        height={height}
        className="rounded-lg shadow-md"
      />
    </div>
  );
};

export const InteractiveGraph: React.FC<InteractiveGraphProps> = ({ 
  src, 
  width = "100%", 
  height = "500px" 
}) => {
  return (
    <div className="relative rounded-lg shadow-md overflow-hidden">
      <iframe
        src={src}
        width={width}
        height={height}
        style={{ border: 'none' }}
      />
    </div>
  );
}; 