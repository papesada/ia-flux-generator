// server/server.js
const express = require('express');
const fetch = require('node-fetch');
require('dotenv').config();
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const path = require('path');

const app = express();
app.use(helmet());
app.use(express.json({ limit: '2mb' }));

// Limiter: very basic rate limiting
const limiter = rateLimit({ windowMs: 60 * 1000, max: 30 });
app.use(limiter);

// Serve static files from project root so index.html can be served
app.use(express.static(path.join(__dirname, '..')));

// Proxy endpoint
app.post('/api/generate', async (req, res) => {
  try {
    const { prompt } = req.body;
    if (!prompt) return res.status(400).json({ error: 'prompt manquant' });

    const promptOptimise = `${prompt}, clear educational illustration, professional pedagogical diagram, bright colors, white background, high resolution, 4k`;

    const hfResp = await fetch('https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.HF_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputs: promptOptimise }),
    });

    if (!hfResp.ok) {
      const text = await hfResp.text();
      return res.status(hfResp.status).send(text);
    }

    const arrayBuffer = await hfResp.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    const contentType = hfResp.headers.get('content-type') || 'application/octet-stream';
    res.set('Content-Type', contentType);
    res.send(buffer);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur lors de la génération' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Proxy server listening on ${PORT}`));
