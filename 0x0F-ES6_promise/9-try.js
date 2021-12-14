export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction(), 'Guardrail was processed');
  } catch (e) {
    queue.push(`Error: ${e.message}`, 'Guardrail was processed');
  }
  return queue;
}
