import React, { useState, useEffect } from 'react';
import { marked } from 'marked';

const ReleaseNotesPage = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    const timeStamp = new Date().getTime();
    fetch(`/Release-notes.md?${timeStamp}`)
      .then(response => response.text())
      .then(text => {
        setMarkdown(marked.parse(text, {sanitize: true}));
      });
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Release Notes</h1>
      <div dangerouslySetInnerHTML={{ __html: markdown }} />
    </div>
  );
}

export default ReleaseNotesPage;
