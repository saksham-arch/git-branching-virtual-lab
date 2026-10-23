import React, {useState} from 'react';
import {createRoot} from 'react-dom/client';
function MergePrediction() {
  const [diverged, setDiverged] = useState(false);
  const [answer, setAnswer] = useState('');
  return <section>
    <h2>Branch history</h2>
    <label><input type="checkbox" checked={diverged} onChange={event => {setDiverged(event.target.checked); setAnswer('');}} /> Main has new commits since the feature branch was created</label>
    <pre>{diverged ? 'A ─ B ─ C  main\n     ╲ D ─ E  feature' : 'A ─ B  main\n     ╲ D ─ E  feature'}</pre>
    <p>Assume the edits do not conflict. What does a default git merge feature do while main is checked out?</p>
    <button onClick={() => setAnswer('fast-forward')}>Fast-forward</button>{' '}
    <button onClick={() => setAnswer('merge commit')}>Create a merge commit</button>
    {answer && <p role="status">{answer === (diverged ? 'merge commit' : 'fast-forward') ? 'Correct. ' : 'Try again. '}{diverged ? 'Both branches advanced, so Git combines their histories with a merge commit.' : 'Main is an ancestor of feature, so Git can advance the main pointer.'}</p>}
    <p><a href="/#merge-practice">Verify in the merge simulation</a></p>
  </section>;
}
createRoot(document.getElementById('root')).render(<MergePrediction />);
