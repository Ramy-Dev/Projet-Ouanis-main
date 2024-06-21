import { writable } from 'svelte/store';

export const alreadySelectedConditions = writable([]);

alreadySelectedConditions.add = (condition) => {
  alreadySelectedConditions.update(conditions => [...conditions, condition]);
};

alreadySelectedConditions.remove = (condition) => {
  alreadySelectedConditions.update(conditions => conditions.filter(c => c !== condition));
};

alreadySelectedConditions.toggle = (condition) => {
  alreadySelectedConditions.update(conditions => {
    if (conditions.includes(condition)) {
      return conditions.filter(c => c !== condition);
    } else {
      return [...conditions, condition];
    }
  });
};