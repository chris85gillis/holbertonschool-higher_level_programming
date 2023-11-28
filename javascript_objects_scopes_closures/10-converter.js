#!/usr/bin/node

egit xports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
