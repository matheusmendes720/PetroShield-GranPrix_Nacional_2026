import React from 'react';
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar, Cell, LineChart, Line
} from 'recharts';

const data = [
  { name: '00:00', threats: 45, blocked: 44, savings: 1200 },
  { name: '04:00', threats: 52, blocked: 52, savings: 1500 },
  { name: '08:00', threats: 88, blocked: 85, savings: 3200 },
  { name: '12:00', threats: 65, blocked: 65, savings: 2100 },
  { name: '16:00', threats: 120, blocked: 118, savings: 5400 },
  { name: '20:00', threats: 95, blocked: 95, savings: 2800 },
];

const COLORS = ['#00f2ff', '#39ff14', '#ff3131', '#FFD700'];

export const ScadaHealthChart: React.FC = () => {

  return (
    <ResponsiveContainer width="100%" height={200}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
        <XAxis dataKey="name" stroke="#ffffff30" fontSize={10} />
        <YAxis stroke="#ffffff30" fontSize={10} />
        <Tooltip contentStyle={{ background: '#0a1929', border: '1px solid #00f2ff30', borderRadius: '8px' }} />
        <Line type="monotone" dataKey="threats" stroke="#00f2ff" strokeWidth={2} dot={false} />
        <Line type="monotone" dataKey="blocked" stroke="#39ff14" strokeWidth={2} dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export const ThreatTrendChart: React.FC = () => (
  <ResponsiveContainer width="100%" height={200}>
    <AreaChart data={data}>
      <defs>
        <linearGradient id="colorThreats" x1="0" y1="0" x2="0" y2="1">
          <stop offset="5%" stopColor="#00f2ff" stopOpacity={0.3} />
          <stop offset="95%" stopColor="#00f2ff" stopOpacity={0} />
        </linearGradient>
      </defs>
      <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
      <XAxis dataKey="name" stroke="#ffffff30" fontSize={10} />
      <YAxis stroke="#ffffff30" fontSize={10} />
      <Tooltip contentStyle={{ background: '#0a1929', border: '1px solid #00f2ff30', borderRadius: '8px' }} />
      <Area type="monotone" dataKey="threats" stroke="#00f2ff" fillOpacity={1} fill="url(#colorThreats)" />
    </AreaChart>
  </ResponsiveContainer>
);

export const SavingsChart: React.FC = () => (
  <ResponsiveContainer width="100%" height={200}>
    <BarChart data={data}>
      <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
      <XAxis dataKey="name" stroke="#ffffff30" fontSize={10} />
      <YAxis stroke="#ffffff30" fontSize={10} />
      <Tooltip contentStyle={{ background: '#0a1929', border: '1px solid #00f2ff30', borderRadius: '8px' }} />
      <Bar dataKey="savings" fill="#39ff14" fillOpacity={0.6} radius={[4, 4, 0, 0]}>
        {data.map((_entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} fillOpacity={0.6} />
        ))}
      </Bar>
    </BarChart>
  </ResponsiveContainer>
);
