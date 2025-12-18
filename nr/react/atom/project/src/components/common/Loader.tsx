import React from 'react';

export function Loader() {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-5 rounded-lg flex items-center space-x-4">
        <div className="animate-spin rounded-full h-8 w-8 border-4 border-indigo-500 border-t-transparent"></div>
        <span className="text-gray-700 font-medium">Loading...</span>
      </div>
    </div>
  );
}